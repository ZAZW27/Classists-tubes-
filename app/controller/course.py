import sys
import json
from PySide6.QtWidgets import *
from course_dashboard_ui import Ui_MainWindow

course = '1'

def load_assigment():
    with open(f"data/courses/{course}/assignment.json", 'r') as file:
        return json.load(file)


def load_note():
    with open(f"data/courses/{course}/note.json", 'r') as file:
        return json.load(file)


def load_courses():
    with open(f"data/courses/{course}/id.json", 'r') as file:
        return json.load(file)

def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # Load all datas
    self.assignment = load_assigment()
    self.courses = load_courses()
    self.note = load_note()

    # Set window title
    self.setWindowTitle(f"{self.courses['title']} - Dashboard")

    # Set the course identity
    lokasi = self.courses["lokasi"] # merge the building and classroom number
    self.ui.course_title_lbl.setText(f"<p align='center'><span style=' font-size:16pt; font-weight:700;'><b>{self.courses['title']}</b></span></p>")
    self.ui.classroom_lbl.setText(f"<b>Ruang Kelas:</b> {''.join(lokasi)}")
    self.ui.session_lbl.setText(f"<b>Sesi:</b> {self.courses['sesi']}")

    # Header buttons connections
    self.ui.return_btn.clicked.connect(self.return_to_dashboard)
    self.ui.edit_btn.clicked.connect(self.edit_course)
    self.ui.del_btn.clicked.connect(self.delete_course)

    # Add to-do and note buttons connections
    self.ui.add_todo_btn.clicked.connect(self.add_todo)
    self.ui.add_note_btn.clicked.connect(self.add_note)

    # Construct the to-do and note items
    self.add_task_frames()
    self.add_note_frames()


def add_task_frames(self):
    """Create frames for each task in the JSON data."""
    for key, task in self.assignment.items():
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
        self.ui.todo_list_lyt.addWidget(frame)


def add_note_frames(self):
    """Create frames for each note in the JSON data."""
    for key, note in self.note.items():
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

        # Add the frame to the main layout
        self.ui.note_list_lyt.addWidget(frame)


def add_todo(self):
    """Going to add to-do page."""
    print("To-do added.")


def add_note(self):
    """Going to add note page."""
    print("Note added.")


def return_to_dashboard(self):
    """Going to return to main dashboard."""
    print("Returning to dashboard.")


def edit_course(self):
    """Going to edit course page."""
    print("Course edited.")


def delete_course(self):
    """Going to delete course page."""
    print("Course deleted.")
