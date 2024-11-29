from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *

# from layout.components.pages.dashboard import Dashboard
import json
import os
from datetime import datetime, timedelta
import locale

def get_course_data(): 
    print("Loading: getting data")
    course_path = "app/data/courses"
    with open("app/data/colors.json", "r") as color_File: # initialize to fetch color data
        fetch_color = json.load(color_File)
        
    courses = {} # temporary courses storgae
    for item in os.listdir(course_path):  # loo[ through out the path folder
        
        # ======== GETTING THE IDENTIFICATION courses ========
        item_path = os.path.join(course_path, item) # get current folder
        if not os.path.isdir(item_path): continue # check if it exists and a directory
        
        id_json_path = os.path.join(item_path, "id.json") # get identification file 
        if not os.path.isfile(id_json_path): continue # skips if it doesn't existst
        
        with open(id_json_path, 'r') as json_file: # Open and read the identification file
            courses[item] = json.load(json_file) # insert the id file into temp courses
        
        # ======== REPLACE THE color_id VALUE ========
        color_id = courses[item]["color_id"] # Get the current color id from temp courses
        try: 
            courses[item]["color_id"] = [fetch_color[color_id][1], fetch_color[color_id][2]] 
        except KeyError: 
            courses[item]["color_id"] = [fetch_color["8"][1], fetch_color["8"][2]] 
        
        # ======== CHECKING FOR ASSIGNMENT FILE ========
        assignment_path = os.path.join(item_path, "assignment.json") # getting assignment's pat
        if not os.path.isfile(assignment_path): # checkning if it exists
            with open(assignment_path, "w") as file: json.dump({}, file, indent=4) # if doesn't exists then create one
        
        with open(assignment_path, 'r') as file: courses[item]['assignment'] = json.load(file) # read and create new key and add its value for assignment

        # ======== CHECKING FOR NOTES FILE ========
        notes_path = os.path.join(item_path, "note.json")
        if not os.path.isfile(notes_path): 
            with open(notes_path, 'w') as file: json.dump({}, file, indent=4)
        
        with open(notes_path, 'r') as file: courses[item]["notes"] = json.load(file)

    sorted_courses = dict(sorted(courses.items(), key=lambda x: get_time_distance(x[1])))
    
    return sorted_courses

def get_time_distance(item):
    import locale
    from datetime import datetime, timedelta
    import json

    locale.setlocale(locale.LC_TIME, "id_ID.UTF-8")
    order_of_days = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

    with open("app/data/sesi.json", "r") as sesi_file:
        fetch_session = json.load(sesi_file)

    hari = item["hari"]
    sesi = item["sesi"]
    sesi_times = fetch_session.get(sesi, ["00:00", "00:00"])  # Get start and end times
    start_time = sesi_times[0]
    end_time = sesi_times[1]

    # Current time and date
    now = datetime.now()
    current_day = now.strftime("%A").lower()

    # Determine days ahead for the target day
    today_index = order_of_days.index(current_day)
    target_index = order_of_days.index(hari)
    days_ahead = (target_index - today_index) % len(order_of_days)

    # Create datetime objects for the session start and end times
    target_date = now + timedelta(days=days_ahead)
    target_start_datetime_str = target_date.strftime(f"%Y-%m-%d {start_time}")
    target_end_datetime_str = target_date.strftime(f"%Y-%m-%d {end_time}")
    target_start_datetime = datetime.strptime(target_start_datetime_str, "%Y-%m-%d %H:%M")
    target_end_datetime = datetime.strptime(target_end_datetime_str, "%Y-%m-%d %H:%M")

    # Time difference calculations
    time_until_start = (target_start_datetime - now).total_seconds()
    time_until_end = (target_end_datetime - now).total_seconds()

    # Assign `status_dot` based on the class timing
    if days_ahead > 0:  # Not today
        item["status_dot"] = "rgb(211, 211, 211)"  # Light grey
    elif days_ahead == 0:  # Today
        if time_until_start > 3600:  # Far (more than 1 hour away)
            item["status_dot"] = "rgb(255, 0, 0)"  # Red
        elif 0 < time_until_start <= 3600:  # Near (within 1 hour)
            item["status_dot"] = "rgb(255, 217, 0)"  # Yellow
        elif time_until_end >= 0:  # Ongoing class
            item["status_dot"] = "rgb(34, 197, 94)"  # Green
        else:  # Class has passed
            item["status_dot"] = "rgb(211, 211, 211)"  # Light grey
    else:  # Shouldn't happen (safety fallback)
        item["status_dot"] = "rgb(211, 211, 211)"  # Light grey

    return time_until_start  # Return time difference until start (if needed)

def generate_course(course_wrapper, courses): 
    # print(f"Creating course for: {course_data['title']}")
    # ================================================
    # ================Create courses==================
    # ================================================
    
    course_widgets = []
    for course_data in courses:
        course = QFrame(course_wrapper)
        course.setObjectName(u"course")
        course.setMinimumSize(QSize(0, 90))
        course.setMaximumSize(QSize(16777215, 90))
        course.setStyleSheet("background:transparent;")
        course.setFrameShape(QFrame.StyledPanel)
        course.setFrameShadow(QFrame.Raised)

        # Load and customize the folder icon
        folder_img_path = os.path.join(os.path.dirname(__file__), "../resources/icons/folder.svg")
        with open(folder_img_path, 'r') as image:
            svg_content = image.read()
        svg_content = svg_content.replace('fill="#cacaca"', f'fill="{courses[course_data].get("color_id", "#cacaca")[0]}"')

        folder_icon = QLabel(course)
        folder_icon.setMinimumSize(70, 70)
        folder_icon.setMaximumSize(70, 70)

        renderer = QSvgRenderer(QByteArray(svg_content.encode()))

        pixmap = QPixmap(70, 70)
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        folder_icon.setPixmap(pixmap)
        folder_icon.setScaledContents(True)

        # Add course details
        course_title = QLabel()
        course_title.setText(courses[course_data].get("title", "Unknown Course"))
        course_title.setStyleSheet("font: 20px; color: rgb(75, 75, 75);")

        session_label = QLabel()
        session_label.setText(courses[course_data].get("sesi", "No Session Info"))
        session_label.setStyleSheet("font: 14px; color: rgb(75, 75, 75);")

        status_dot = QFrame()
        status_dot.setMinimumSize(16, 16)
        status_dot.setMaximumSize(16, 16)
        color = courses[course_data].get("status_dot", "rgb(255, 0, 0)")
        status_dot.setStyleSheet(f"background: {color}; border-radius: 8px")
        complete = QLabel()
        complete.setText("apa aja ini")
        
        incomplete = QLabel()
        incomplete.setText("apa aja ini")
        
        separator = QFrame()
        separator.setMinimumHeight(5)
        separator.setStyleSheet(f"""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                    stop:0 {courses[course_data].get("color_id", "#cacaca")[0]}, 
                    stop:1 {courses[course_data].get("color_id", "#cacaca")[1]});
            border: none;
        """)

        # Layouting
        course_layout = QVBoxLayout(course)

        course_top_vertical = QVBoxLayout()
        assignment_layout = QHBoxLayout()
        
        course_top_layout = QHBoxLayout()
        course_top_layout.setSpacing(10)
        course_top_layout.addWidget(folder_icon)
        
        course_text_layout = QVBoxLayout()
        course_text_layout.addWidget(course_title)
        course_text_layout.addWidget(session_label)

        course_top_layout.addWidget(status_dot, alignment=Qt.AlignTop)
        course_top_layout.addLayout(course_top_vertical)
        
        course_top_vertical.addLayout(course_text_layout)
        course_top_vertical.addLayout(assignment_layout)
        
        assignment_layout.addWidget(complete)
        assignment_layout.addWidget(incomplete)
        
        course_layout.addLayout(course_top_layout)
        course_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        course_layout.addWidget(separator)

        course_widgets.append(course)

    return course_widgets