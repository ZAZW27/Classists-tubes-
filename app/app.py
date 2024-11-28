# app/app.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from layout.index import Ui_MainWindow
from PySide6.QtCore import QSize
from layout.components.taskbar import TaskBar  
from controller.dashboard import setup_dashboard

def setup_ui():
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)  # Memanggil setupUI dari index.py

    setup_dashboard(main_window, ui)

    # GETTING TASKBAR
    task_bar = TaskBar(main_window)
    ui.gridLayout_2.addWidget(task_bar, 1, 0, 1, 1)

    main_window.show()
    return main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = setup_ui()  # Set up the UI
    sys.exit(app.exec_())  # Start the app event loop
