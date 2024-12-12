# taskbar.py
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *

from controller.incomplete import *

class Incomplete(QFrame):
        def __init__(self, parent=None, click_todo_btn=None):
                super().__init__(parent)
                
                self.click_todo_btn = click_todo_btn
                                
                self.setObjectName(u"wrapper")
                self.setGeometry(QRect(0, 0, 679, 1037))
                self.gridLayout = QGridLayout(self)
                self.gridLayout.setObjectName(u"gridLayout")
                self.gridLayout.setHorizontalSpacing(0)
                self.gridLayout.setVerticalSpacing(12)
                self.gridLayout.setContentsMargins(0, 0, 0, 0)
                self.container = QFrame(self)
                self.container.setObjectName(u"container")
                sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
                self.container.setSizePolicy(sizePolicy)
                self.container.setMaximumSize(QSize(650, 16777215))
                self.container.setStyleSheet(u"")
                self.container.setFrameShape(QFrame.StyledPanel)
                self.container.setFrameShadow(QFrame.Raised)
                self.verticalLayout_3 = QVBoxLayout(self.container)
                self.verticalLayout_3.setSpacing(12)
                self.verticalLayout_3.setObjectName(u"verticalLayout_3")
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)


                sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)

                self.course_container = QFrame(self)
                self.course_container.setObjectName(u"course_container")
                sizePolicy.setHeightForWidth(self.course_container.sizePolicy().hasHeightForWidth())
                self.course_container.setSizePolicy(sizePolicy)
                self.course_container.setStyleSheet(u"border-top-left-radius: 50px;\n"
        "border-top-right-radius: 50px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "background: rgb(255, 255, 255);\n"
        )
                self.course_container.setFrameShape(QFrame.StyledPanel)
                self.course_container.setFrameShadow(QFrame.Raised)
                self.verticalLayout_5 = QVBoxLayout(self.course_container)
                self.verticalLayout_5.setSpacing(25)
                self.verticalLayout_5.setObjectName(u"verticalLayout_5")
                self.verticalLayout_5.setContentsMargins(15, 20, 15, 12)
                self.title_course = QFrame(self.course_container)
                self.title_course.setObjectName(u"title_course")
                sizePolicy.setHeightForWidth(self.title_course.sizePolicy().hasHeightForWidth())
                self.title_course.setSizePolicy(sizePolicy)
                self.title_course.setFrameShape(QFrame.StyledPanel)
                self.title_course.setFrameShadow(QFrame.Raised)
                self.horizontalLayout = QHBoxLayout(self.title_course)
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.line_course = QFrame(self.title_course)
                self.line_course.setObjectName(u"line_course")
                self.line_course.setMinimumSize(QSize(0, 5))
                self.line_course.setMaximumSize(QSize(16777215, 5))
                self.line_course.setStyleSheet(u"background: rgb(65, 225, 182); border-radius: 20px;")
                self.line_course.setFrameShape(QFrame.StyledPanel)
                self.line_course.setFrameShadow(QFrame.Raised)

                self.horizontalLayout.addWidget(self.line_course)

                self.label = QLabel(self.title_course)
                self.label.setObjectName(u"label")
                sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
                self.label.setSizePolicy(sizePolicy1)
                # self.label.setFont(font)
                self.label.setStyleSheet(u"color: rgb(88, 89, 89);")

                self.horizontalLayout.addWidget(self.label)

                self.line_course_2 = QFrame(self.title_course)
                self.line_course_2.setObjectName(u"line_course_2")
                self.line_course_2.setMinimumSize(QSize(0, 5))
                self.line_course_2.setMaximumSize(QSize(16777215, 5))
                self.line_course_2.setStyleSheet(u"background: rgb(65, 225, 182); border-radius: 50px;")
                self.line_course_2.setFrameShape(QFrame.StyledPanel)
                self.line_course_2.setFrameShadow(QFrame.Raised)

                self.horizontalLayout.addWidget(self.line_course_2)


                self.verticalLayout_5.addWidget(self.title_course)

                self.course_wrapper = QFrame(self.course_container)
                self.course_wrapper.setObjectName(u"course_wrapper")
                sizePolicy.setHeightForWidth(self.course_wrapper.sizePolicy().hasHeightForWidth())
                self.course_wrapper.setSizePolicy(sizePolicy)
                self.course_wrapper.setStyleSheet(u"\n"
        "border-radius: 0;")
                self.course_wrapper.setFrameShape(QFrame.StyledPanel)
                self.course_wrapper.setFrameShadow(QFrame.Raised)
                self.courses_layout = QVBoxLayout(self.course_wrapper)
                self.courses_layout.setSpacing(20)
                self.courses_layout.setObjectName(u"courses_layout")
                self.courses_layout.setContentsMargins(0, 0, 0, 0)
                
                # # ================================================
                # # ============Create couser STARTses==============
                # # ================================================
                course_data = get_todo_data()
                
                course_widgets = generate_todo(self.course_wrapper, course_data, click_todo_btn=lambda data: self.call_back(data))
                for course_widget in course_widgets: 
                        self.courses_layout.addWidget(course_widget)


                self.verticalLayout_5.addWidget(self.course_wrapper)

                self.gridLayout.addWidget(self.course_container, 1, 0, 1, 1)
                
                self.label.setText(QCoreApplication.translate("MainWindow", u"Assignments", None))
                self.course_wrapper.setAccessibleName("")
        
        def call_back(self, data): 
                if self.click_todo_btn: 
                        self.click_todo_btn(data['course_id'], data['assignment_id'])