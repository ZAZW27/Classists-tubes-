import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize
from layout.index import Ui_MainWindow
from layout.components.taskbar import TaskBar  
from layout.components.pages.dashboard import Dashboard
from layout.components.pages.note import Note


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

def setup_taskbar(main_window, ui): 
    task_bar = TaskBar(main_window, task_click_callback=lambda task_id: handle_page_toggle(task_id, ui, main_window))

    ui.gridLayout_2.addWidget(task_bar, 1, 0, 1, 1)

def setup_dashboard(main_window, ui):
    wrapper = Dashboard(main_window)
    ui.mainScroll.setWidget(wrapper)
    ui.gridLayout_2.addWidget(ui.mainScroll, 0, 0, 1, 1)

def setup_note_edit(main_window, ui): 
    wrapper = Note(main_window)
    ui.mainScroll.setWidget(wrapper)
    ui.gridLayout_2.addWidget(ui.mainScroll, 0, 0, 1, 1)

def setup_other_page(main_window, ui):
    pass

def handle_page_toggle(task_id, ui, main_window):
    global page 
    print(f"Task clicked: {task_id}")

    page = task_id
    current_widget = ui.mainScroll.widget()
    if current_widget:
        current_widget.deleteLater()

    if page == 1:
        setup_dashboard(main_window, ui)
    else:
        print("clicked")
        setup_note_edit(main_window, ui)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window, ui = setup_ui()
    sys.exit(app.exec_())
