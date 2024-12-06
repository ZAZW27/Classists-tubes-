import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
from layout.index import Ui_MainWindow
from layout.components.taskbar import TaskBar  
from layout.components.pages.dashboard import Dashboard
from layout.components.pages.note import Note
from layout.components.pages.course import Course
import json
import shutil
import os

# ==============================================================================
# ------------------------------INITIALIZE PROGRAM------------------------------
# ==============================================================================
page = 1
def setup_ui():
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)  # Memanggil setupUI dari index.py

    setup_dashboard(main_window, ui)
    # setup_note_edit(main_window, ui)

    # GETTING TASKBAR
    setup_taskbar(main_window, ui)

    main_window.show()
    return main_window, ui  # Return both the main_window and ui

# ==============================================================================
# ------------------------------GETTING COMPONENT-------------------------------
# ==============================================================================

# ------------------- GET TASKBAR COMPONENT
def setup_taskbar(main_window, ui): 
    task_bar = TaskBar(main_window, task_click_callback=lambda task_id: handle_page_toggle(task_id, ui, main_window))

    ui.gridLayout_2.addWidget(task_bar, 1, 0, 1, 1)

# ------------------- GET DASHBOARD COMPONENT
def setup_dashboard(main_window, ui):
    wrapper = Dashboard(main_window, course_click_callback=lambda course_id: get_course_data(course_id, ui, main_window))
    ui.mainScroll.setWidget(wrapper)
    ui.gridLayout_2.addWidget(ui.mainScroll, 0, 0, 1, 1)

# ------------------- GET COURSE COMPONENT
def setup_course(main_window, ui, course_id): 
    course_wrapper = Course(main_window, course_id)
    ui.mainScroll.setWidget(course_wrapper)
    
    with open(f"app/data/courses/{course_id}/assignment.json", 'r') as file:
        assignment = json.load(file)
    with open(f"app/data/courses/{course_id}/id.json", 'r') as file:
        courses = json.load(file)
    with open(f"app/data/courses/{course_id}/note.json", 'r') as file:
        note = json.load(file)
    
    # setWindowTitle(f"{courses['title']} - Dashboard")

    # Set the course identity
    lokasi = courses["lokasi"] # merge the building and classroom number
    course_wrapper.course_title_lbl.setText(f"<p align='center'><span style=' font-size:16pt; font-weight:700;'><b>{courses['title']}</b></span></p>")
    course_wrapper.classroom_lbl.setText(f"<b>Ruang Kelas:</b> {''.join(lokasi)}")
    course_wrapper.session_lbl.setText(f"<b>Sesi:</b> {courses['sesi']}")

    # Header buttons connections
    course_wrapper.return_btn.clicked.connect(lambda: return_to_dashboard(main_window, ui))
    # course_wrapper.edit_btn.clicked.connect(edit_course)
    course_wrapper.del_btn.clicked.connect(lambda: delete_course(course_id, main_window, ui))

    # # Add to-do and note buttons connections
    # course_wrapper.add_todo_btn.clicked.connect(add_todo)
    # course_wrapper.add_note_btn.clicked.connect(add_note)/

    # Construct the to-do and note items
    add_task_frames(assignment, course_wrapper)
    
    for key, notes in note.items():
        add_note_frames(notes, key, course_id, course_wrapper, main_window, ui)

def add_task_frames(assignment, course_wrapper):
    """Create frames for each task in the JSON data."""
    for key, task in assignment.items():
        title = task.get("title")
        description = task.get("deskripsi")
        deadline = task.get("deadline")
        is_finished = task.get("isFinished")

        # Create a frame for the task
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: lightyellow; padding: 10px; margin: 5px;")
        layout = QVBoxLayout(frame)

        # Add task details as labels
        layout.addWidget(QLabel(f"<b>Tugas {key}:</b> {title}"))
        layout.addWidget(QLabel(f"<b>Deskripsi:</b> {description}"))
        layout.addWidget(QLabel(f"<b>Tenggat pengumpulan:</b> {deadline}"))
        layout.addWidget(QLabel(f"<b>Ditandai selesai:</b> {'Ya' if is_finished else 'Tidak'}"))

        # Add the frame to the main layout
        course_wrapper.todo_list_lyt.addWidget(frame)

def add_note_frames(note, key, course_id, course_wrapper, main_window, ui):
    """Create frames for each note in the JSON data."""
    
    title = note.get("title")
    description = note.get("deskripsi")
    created_at = note.get("created_at")

    # Create a frame for the note
    frame = QFrame()
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setStyleSheet("background-color: lightyellow; padding: 10px; margin: 5px;")
    layout = QVBoxLayout(frame)

    # Add note details as labels
    description_lbl = QLabel(f"<b>Isi:</b> {description}")
    description_lbl.setWordWrap(True)
    layout.addWidget(QLabel(f"<b>Catatan {key}:</b> {title}"))
    layout.addWidget(description_lbl)
    layout.addWidget(QLabel(f"<b>Dibuat pada:</b> {created_at}"))

    course_wrapper.note_list_lyt.addWidget(frame)
    
    frame.mousePressEvent = lambda event: setup_note_edit(main_window, ui, course_id, key)

def delete_course(course_id, main_window, ui):
    reply = QMessageBox.question(
        None,  # Parent (None means it's a standalone dialog)
        "Confirm Deletion",
        f"Are you sure you want to delete the course with ID {course_id}?",
        QMessageBox.Yes | QMessageBox.No
    )
    if reply != QMessageBox.Yes :return print("Cancel penghapusan ")
    
    try: 
        path = f"app/data/courses/{course_id}"
        os.listdir(path)
        
        print("file exists")
        shutil.rmtree(path)
        change_page(main_window, ui)
        
    except FileNotFoundError: 
        return print("File not found :(")

def return_to_dashboard(main_window, ui):
        global page
        page = 1
        change_page(main_window, ui)

# ------------------- GET NOTES COMPONENT
def setup_note_edit(main_window, ui, course_id, note_id): 
    with open(f"app/data/courses/{course_id}/id.json", 'r') as file:
        title = json.load(file)["title"]
        
    wrapper = Note(main_window, note_id, title, course_id, ui, lambda: setup_note_edit(main_window, ui, course_id, note_id))
    ui.mainScroll.setWidget(wrapper)
    ui.gridLayout_2.addWidget(ui.mainScroll, 0, 0, 1, 1)

# ==============================================================================
# ------------------------------HANDLE PAGE CANGE-------------------------------
# ==============================================================================

# ------------------- TASKBAR BUTTONS
def handle_page_toggle(task_id, ui, main_window):
    global page 
    print(f"Task clicked: {task_id}")

    page = task_id
    current_widget = ui.mainScroll.widget()
    if current_widget:
        current_widget.deleteLater()
    change_page(main_window, ui)
    
def get_course_data(course_id, ui, main_window): 
    if course_id == 0: 
        change_page(main_window, ui)
    else: 
        current_widget = ui.mainScroll.widget()
        if current_widget:
            current_widget.deleteLater()
        
        setup_course(main_window, ui, course_id)

def change_page(main_window, ui): 
    global page 
    if page == 1:
        setup_dashboard(main_window, ui)

# ==============================================================================
# ------------------------------STARTING PROGRAM--------------------------------
# ==============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window, ui = setup_ui()
    sys.exit(app.exec())
