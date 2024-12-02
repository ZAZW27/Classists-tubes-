# app/app.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize
from layout.index import Ui_MainWindow
from layout.components.taskbar import TaskBar  
from layout.components.pages.dashboard import Dashboard

# Global variable to store the current page
page = 0

def setup_ui():
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)  # Memanggil setupUI dari index.py

    # GETTING DASHBOARD or other page based on the 'page' variable
    if page == 1: 
        setup_dashboard(main_window, ui)
    else:
        setup_other_page(main_window, ui)

    # GETTING TASKBAR
    setup_taskbar(main_window, ui)

    main_window.show()
    return main_window

def setup_taskbar(main_window, ui): 
    # Pass the callback function to TaskBar
    task_bar = TaskBar(main_window, task_click_callback=handle_page_toggle)
    ui.gridLayout_2.addWidget(task_bar, 1, 0, 1, 1)

def setup_dashboard(main_window, ui):
    wrapper = Dashboard(main_window)
    ui.mainScroll.setWidget(wrapper)
    ui.gridLayout_2.addWidget(ui.mainScroll, 0, 0, 1, 1)

def setup_other_page(main_window, ui):
    # This method will load another layout when 'page' changes.
    pass

def handle_page_toggle(task_id):
    global page  # To modify the global 'page' variable
    print(f"Task clicked: {task_id}")

    # Change the page based on the task_id
    page = task_id  # Assuming task_id corresponds to a specific page, e.g., 1 = Dashboard, 2 = Other Page

    # Re-initialize the UI to reflect the change in page
    main_window = QApplication.instance().activeWindow()  # Get the current window instance
    main_window.close()  # Close the current window to refresh the UI
    setup_ui()  # Call the setup_ui function to reload the UI based on the new page variable

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = setup_ui()  # Set up the UI
    sys.exit(app.exec_())  # Start the app event loop
