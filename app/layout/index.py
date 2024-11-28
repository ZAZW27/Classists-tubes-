import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *
from layout.components.taskbar import TaskBar
from layout.components.pages.dashboard import Dashboard

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 655)
        MainWindow.setStyleSheet(u"background:rgb(235, 244, 246);\n"
"border:0;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mainScroll = QScrollArea(self.centralwidget)
        self.mainScroll.setObjectName(u"mainScroll")
        self.mainScroll.setMaximumSize(QSize(700, 16777215))
        self.mainScroll.setStyleSheet(u"QScrollBar:vertical{\n"
"	background: rgb(204, 211, 213);\n"
"	border: none;\n"
"	width: 5px;\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background:rgb(150, 150, 150);\n"
"	border-radius: 10px;\n"
"	min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar{\n"
"padding: 0px;\n"
"margin: 0px;\n"
"}")
        self.mainScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mainScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainScroll.setWidgetResizable(True)
        
        # GETTING DASHBOARD
        self.wrapper = Dashboard(MainWindow)
        
        self.mainScroll.setWidget(self.wrapper)

        self.gridLayout_2.addWidget(self.mainScroll, 0, 0, 1, 1)

        # GETTING TASKBAR
        task_bar = TaskBar(MainWindow)
        self.gridLayout_2.addWidget(task_bar, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))