# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designGaEhLN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(636, 661)
        MainWindow.setStyleSheet(u"background-color: rgb(235, 244, 246);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(500, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.wrapper = QWidget()
        self.wrapper.setObjectName(u"wrapper")
        self.wrapper.setGeometry(QRect(0, 0, 498, 570))
        self.gridLayout = QGridLayout(self.wrapper)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.wrapper)
        self.container.setObjectName(u"container")
        self.container.setMaximumSize(QSize(500, 16777215))
        self.container.setStyleSheet(u"")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.jumbotron = QFrame(self.container)
        self.jumbotron.setObjectName(u"jumbotron")
        self.jumbotron.setMinimumSize(QSize(0, 400))
        self.jumbotron.setMaximumSize(QSize(16777164, 400))
        self.jumbotron.setStyleSheet(u"background: rgb(29, 237, 255);")
        self.jumbotron.setFrameShape(QFrame.StyledPanel)
        self.jumbotron.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.jumbotron)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.datetime = QFrame(self.jumbotron)
        self.datetime.setObjectName(u"datetime")
        self.datetime.setMinimumSize(QSize(0, 60))
        self.datetime.setMaximumSize(QSize(16777215, 60))
        self.datetime.setFrameShape(QFrame.StyledPanel)
        self.datetime.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.datetime)

        self.map = QFrame(self.jumbotron)
        self.map.setObjectName(u"map")
        self.map.setMinimumSize(QSize(0, 300))
        self.map.setMaximumSize(QSize(16777215, 400))
        self.map.setFrameShape(QFrame.StyledPanel)
        self.map.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.map)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.img = QLabel(self.map)
        self.img.setObjectName(u"img")
        self.img.setMinimumSize(QSize(0, 300))
        self.img.setPixmap(QPixmap(u"C:/Users/USER/.designer/backup/img/peta temporary.jpg"))
        self.img.setScaledContents(True)
        self.img.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.img, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.map)


        self.verticalLayout_3.addWidget(self.jumbotron)

        self.kelas = QFrame(self.container)
        self.kelas.setObjectName(u"kelas")
        self.kelas.setStyleSheet(u"background: rgb(255, 217, 24);")
        self.kelas.setFrameShape(QFrame.StyledPanel)
        self.kelas.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.kelas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.course = QFrame(self.kelas)
        self.course.setObjectName(u"course")
        self.course.setMinimumSize(QSize(0, 100))
        self.course.setMaximumSize(QSize(16777215, 100))
        self.course.setLayoutDirection(Qt.LeftToRight)
        self.course.setAutoFillBackground(False)
        self.course.setStyleSheet(u"background: rgb(255, 0, 0);")
        self.course.setFrameShape(QFrame.StyledPanel)
        self.course.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.course)


        self.verticalLayout_3.addWidget(self.kelas, 0, Qt.AlignTop)


        self.gridLayout.addWidget(self.container, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.wrapper)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setStyleSheet(u"background: rgb(44, 255, 114);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img.setText("")
    # retranslateUi

