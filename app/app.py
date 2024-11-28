# from pages import main
import sys
# import pyside6
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout
from PySide6.QtCore import QSize
from layout.index import Ui_MainWindow
from PySide6.QtGui import QFont


def setup_ui():
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    # get_courses(ui)

    main_window.show()
    return main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = setup_ui()
    sys.exit(app.exec_())
