# taskbar.py
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *

class Dashboard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
