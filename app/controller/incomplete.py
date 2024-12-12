from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *

# from layout.components.pages.dashboard import Dashboard
import json
import os
from datetime import datetime, timedelta
import locale

def get_todo_data(): 
    path = "app/data/courses"

    todos = os.listdir(path)

    assignment_mix = {}
    for todo in todos:
        with open(f"{path}/{todo}/assignment.json", 'r') as file:
            data = json.load(file)
            for assignment in data: 
                data[assignment]['course_id'] = todo
                data[assignment]['assignment_id'] = assignment
                
                with open(f"{path}/{todo}/id.json", 'r') as identify: 
                    color_id = json.load(identify)['color_id']
                    with open("app/data/colors.json", 'r') as color: 
                        colors = json.load(color).get(color_id, ["grey", "rgb(202, 202, 202)", "rgb(235, 235, 235)"])
                        data[assignment]['color_id'] = [colors[1], colors[2]]
        assignment_mix[todo] = data

    assignment_sort = []

    for folder in assignment_mix.values():
        for _, task in folder.items():
            if task["isFinished"] == False: assignment_sort.append(task)

    for task in assignment_sort:
        task["deadline"] = datetime.strptime(task["deadline"], "%d/%m/%Y")

    # Step 3: Sort assignment_sort by deadline
    assignment_sort = sorted(assignment_sort, key=lambda x: x["deadline"])

    # Step 4: Optionally, convert datetime back to string
    for task in assignment_sort:
        task["deadline"] = task["deadline"].strftime("%d/%m/%Y")

    for i in assignment_sort: 
        if i['deadline'] == datetime.today().strftime("%d/%m/%Y"): 
            print(i)

    return assignment_sort

def todo_clicked_signal(todo_id, click_todo_btn): 
    if click_todo_btn: 
        click_todo_btn(todo_id)

def generate_todo(todo_wrapper, todos, click_todo_btn=None): 
    todo_widgets = []
    for todo_data in todos:
        generate_each_todo(todo_widgets, todo_wrapper, todo_data, click_todo_btn)

    return todo_widgets
from datetime import datetime, timedelta

def generate_each_todo(todo_widgets, todo_wrapper, todo_data, click_todo_btn): 
    print(todo_data)
    
    # Parse the deadline from the todo_data
    deadline_str = todo_data.get("deadline", "")
    deadline_date = datetime.strptime(deadline_str, "%d/%m/%Y") if deadline_str else None
    today = datetime.now()

    # Calculate days remaining
    days_remaining = (deadline_date - today).days if deadline_date else None

    # Determine status color based on days remaining
    if days_remaining is not None:
        if days_remaining < 0:
            color = "rgb(255, 0, 0)"  # Red for overdue
        elif days_remaining <= 3:
            color = "rgb(255, 217, 0)"  # Yellow for 3 days or less
        else:
            color = "rgb(34, 197, 94)"  # Green for more than 3 days
    else:
        color = "rgb(128, 128, 128)"  # Gray for no deadline info

    # Create the "todo" widget
    todo = QFrame(todo_wrapper)
    todo.setObjectName(u"todo")
    todo.setMinimumSize(QSize(0, 90))
    todo.setMaximumSize(QSize(16777215, 90))
    todo.setStyleSheet(f"background: transparent;")
    todo.setFrameShape(QFrame.StyledPanel)
    todo.setFrameShadow(QFrame.Raised)

    todo_title = QLabel()
    todo_title.setText(todo_data.get("title", "Unknown todo"))
    todo_title.setStyleSheet("font: 20px; color: rgb(75, 75, 75);")
    todo_title.setMinimumHeight(20)

    session_label = QLabel()
    session_label.setText(todo_data.get("deadline", "No deadline info"))
    session_label.setStyleSheet("font: 14px; color: rgb(75, 75, 75);")

    status_dot = QFrame()
    status_dot.setFixedSize(16, 16) 
    status_dot.setStyleSheet(f"background: {color}; border-radius: 8px")
    
    separator = QFrame()
    separator.setMinimumHeight(5)
    separator.setStyleSheet(f"""
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                stop:0 {todo_data.get("color_id", "#cacaca")[0]}, 
                stop:1 {todo_data.get("color_id", "#cacaca")[1]});
        border: none;
    """)

    # Layouting
    todo_layout = QVBoxLayout(todo)
    
    todo_text_wrapper = QFrame()
    
    todo_top_vertical = QVBoxLayout()
    
    todo_top_layout = QHBoxLayout()
    todo_top_layout.setSpacing(10)
    
    todo_text_layout = QVBoxLayout()
    todo_text_layout.addWidget(todo_title)
    todo_text_layout.addWidget(session_label)

    todo_top_layout.addWidget(status_dot, alignment=Qt.AlignTop)
    todo_top_layout.addLayout(todo_top_vertical)
    
    todo_text_wrapper.setLayout(todo_text_layout)
    todo_top_vertical.addWidget(todo_text_wrapper)
    
    todo_layout.addLayout(todo_top_layout)
    todo_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    todo_layout.addWidget(separator)
    
    todo.mousePressEvent = lambda event: todo_clicked_signal(todo_data, click_todo_btn)
    
    todo_widgets.append(todo)
