# app/app.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize
from layout.index import Ui_MainWindow
from layout.components.taskbar import TaskBar  
from layout.components.pages.dashboard import Dashboard

def setup_ui():
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)  # Memanggil setupUI dari index.py

    # GETTING DASHBOARD
    setup_dashboard(main_window, ui)

    # GETTING TASKBAR
    setup_taskbar(main_window, ui)

    main_window.show()
    return main_window

def setup_taskbar(main_window, ui): 
    task_bar = TaskBar(main_window)
    ui.gridLayout_2.addWidget(task_bar, 1, 0, 1, 1)

def setup_dashboard(main_window, ui):
    wrapper = Dashboard(main_window)
    ui.mainScroll.setWidget(wrapper)
    ui.gridLayout_2.addWidget(ui.mainScroll, 0, 0, 1, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = setup_ui()  # Set up the UI
    sys.exit(app.exec_())  # Start the app event loop
