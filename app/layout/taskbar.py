# taskbar.py
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *

class TaskBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up task bar layout
        self.setObjectName("task_bar")
        self.setMinimumSize(QSize(0, 68))
        self.setMaximumSize(QSize(16777215, 90))
        self.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(52, 211, 153), stop:1 rgb(110, 231, 183));"
            "border-radius: 20px;"
        )
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        # Horizontal Layout
        self.horizontalLayout = QHBoxLayout(self)
        
        # Create and add individual task frames (Task_frame_1, Task_frame_2, etc.)
        self.create_task("Task 1", "resources/icons/dashboard.svg")
        self.create_task("Task 2", "")

    def create_task(self, task_name, icon_path):
        task_frame = QFrame(self)
        task_frame.setMinimumSize(QSize(55, 55))
        task_frame.setMaximumSize(QSize(55, 55))
        task_frame.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(67, 202, 153), stop:1 rgb(122, 250, 200));"
            "border-radius: 25px;"
        )
        task_frame.setFrameShape(QFrame.StyledPanel)
        task_frame.setFrameShadow(QFrame.Raised)

        horizontal_layout = QHBoxLayout(task_frame)
        task_label = QLabel(task_frame)
        task_label.setMinimumSize(QSize(40, 40))
        task_label.setMaximumSize(QSize(40, 40))
        task_label.setStyleSheet("background: rgba(255, 255, 255, 0);")
        if icon_path:
            task_label.setPixmap(QPixmap(icon_path))
        task_label.setScaledContents(True)

        horizontal_layout.addWidget(task_label)
        self.horizontalLayout.addWidget(task_frame)
