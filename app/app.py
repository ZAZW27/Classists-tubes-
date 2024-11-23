from pages import main
import sys
# import pyside6
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout
from PySide6.QtCore import QSize
from layout.index import Ui_MainWindow
from PySide6.QtGui import QFont



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = main.setup_ui()
    sys.exit(app.exec_())
