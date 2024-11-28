import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvg import *
from .components.taskbar import TaskBar

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
        self.wrapper = QWidget()
        
        self.wrapper.setObjectName(u"wrapper")
        self.wrapper.setGeometry(QRect(0, 0, 679, 1037))
        self.gridLayout = QGridLayout(self.wrapper)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.wrapper)
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
        self.map_scroll = QScrollArea(self.map)
        self.map_scroll.setObjectName(u"map_scroll")
        self.map_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 650, 333))
        self.map_scroll.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.map_scroll, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.map)


        self.verticalLayout_3.addWidget(self.jumbotron)

        self.assignments = QFrame(self.container)
        self.assignments.setObjectName(u"assignments")
        self.assignments.setMinimumSize(QSize(0, 110))
        self.assignments.setStyleSheet(u"background:rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.assignments.setFrameShape(QFrame.StyledPanel)
        self.assignments.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.assignments)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.title_ass = QFrame(self.assignments)
        self.title_ass.setObjectName(u"title_ass")
        sizePolicy.setHeightForWidth(self.title_ass.sizePolicy().hasHeightForWidth())
        self.title_ass.setSizePolicy(sizePolicy)
        self.title_ass.setFrameShape(QFrame.StyledPanel)
        self.title_ass.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_ass)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_course_9 = QFrame(self.title_ass)
        self.line_course_9.setObjectName(u"line_course_9")
        self.line_course_9.setMinimumSize(QSize(0, 5))
        self.line_course_9.setMaximumSize(QSize(16777215, 5))
        self.line_course_9.setStyleSheet(u"background: rgb(65, 225, 182); border-radius: 20px;")
        self.line_course_9.setFrameShape(QFrame.StyledPanel)
        self.line_course_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.line_course_9)

        self.ass_tit = QLabel(self.title_ass)
        self.ass_tit.setObjectName(u"ass_tit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ass_tit.sizePolicy().hasHeightForWidth())
        self.ass_tit.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(QFont.Weight.Bold)
        self.ass_tit.setFont(font)
        self.ass_tit.setStyleSheet(u"color: rgb(88, 89, 89);")

        self.horizontalLayout_5.addWidget(self.ass_tit)

        self.line_course_10 = QFrame(self.title_ass)
        self.line_course_10.setObjectName(u"line_course_10")
        self.line_course_10.setMinimumSize(QSize(0, 5))
        self.line_course_10.setMaximumSize(QSize(16777215, 5))
        self.line_course_10.setStyleSheet(u"background: rgb(65, 225, 182); border-radius: 50px;")
        self.line_course_10.setFrameShape(QFrame.StyledPanel)
        self.line_course_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.line_course_10)


        self.verticalLayout.addWidget(self.title_ass)

        self.assignments_scroll = QScrollArea(self.assignments)
        self.assignments_scroll.setObjectName(u"assignments_scroll")
        self.assignments_scroll.setMinimumSize(QSize(0, 50))
        self.assignments_scroll.setMaximumSize(QSize(16777215, 60))
        self.assignments_scroll.setStyleSheet(u"QScrollBar:horizontal{\n"
"	border: 0;\n"
"	height: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"	background: rgb(158, 174, 186);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	height: 10px;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal:hover{\n"
"	height: 10px;\n"
"}")
        self.assignments_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.assignments_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.assignments_scroll.setWidgetResizable(True)
        self.assignments_scroll.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ass_scroll_grid = QWidget()
        self.ass_scroll_grid.setObjectName(u"ass_scroll_grid")
        self.ass_scroll_grid.setGeometry(QRect(0, 0, 628, 60))
        self.horizontalLayout_4 = QHBoxLayout(self.ass_scroll_grid)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Assignments_7 = QWidget(self.ass_scroll_grid)
        self.Assignments_7.setObjectName(u"Assignments_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Assignments_7.sizePolicy().hasHeightForWidth())
        self.Assignments_7.setSizePolicy(sizePolicy2)
        self.Assignments_7.setMinimumSize(QSize(150, 0))
        self.Assignments_7.setStyleSheet(u"background: rgb(30, 229, 166);")
        self.gridLayout_17 = QGridLayout(self.Assignments_7)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.ass_text = QLabel(self.Assignments_7)
        self.ass_text.setObjectName(u"ass_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ass_text.sizePolicy().hasHeightForWidth())
        self.ass_text.setSizePolicy(sizePolicy3)
        self.ass_text.setStyleSheet(u"font: 500 14px \"Arial\";\n"
"color: rgb(75, 75, 75);")
        self.ass_text.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.ass_text, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.Assignments_7)

        self.assignments_scroll.setWidget(self.ass_scroll_grid)

        self.verticalLayout.addWidget(self.assignments_scroll)


        self.verticalLayout_3.addWidget(self.assignments)

        self.Note_container = QFrame(self.container)
        self.Note_container.setObjectName(u"Note_container")
        self.Note_container.setMinimumSize(QSize(0, 225))
        self.Note_container.setStyleSheet(u"border:0;")
        self.Note_container.setFrameShape(QFrame.StyledPanel)
        self.Note_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Note_container)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.note_scroll = QScrollArea(self.Note_container)
        self.note_scroll.setObjectName(u"note_scroll")
        self.note_scroll.setStyleSheet(u"QScrollArea {\n"
"    background: rgb(0, 240, 0); /* Entire scroll container background */\n"
"    border: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 0px;\n"
"    height: 5px;\n"
"    background: rgb(220, 220, 220); /* Scrollbar track background */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(158, 174, 186); /* Scrollbar handle */\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.note_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.note_scroll.setWidgetResizable(True)
        self.note_scroll_grid = QWidget()
        self.note_scroll_grid.setObjectName(u"note_scroll_grid")
        self.note_scroll_grid.setGeometry(QRect(0, 0, 651, 222))
        self.gridLayout_5 = QGridLayout(self.note_scroll_grid)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.note_wrapper = QFrame(self.note_scroll_grid)
        self.note_wrapper.setObjectName(u"note_wrapper")
        sizePolicy.setHeightForWidth(self.note_wrapper.sizePolicy().hasHeightForWidth())
        self.note_wrapper.setSizePolicy(sizePolicy)
        self.note_wrapper.setMinimumSize(QSize(0, 200))
        self.note_wrapper.setStyleSheet(u"")
        self.note_wrapper.setFrameShape(QFrame.StyledPanel)
        self.note_wrapper.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.note_wrapper)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.note = QFrame(self.note_wrapper)
        self.note.setObjectName(u"note")
        self.note.setMinimumSize(QSize(300, 0))
        self.note.setMaximumSize(QSize(300, 16777215))
        self.note.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(57, 254, 132), stop:1 rgb(30, 229, 166));\n"
"\n"
"border-radius: 10px;")
        self.note.setFrameShape(QFrame.StyledPanel)
        self.note.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.note)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.note)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(75, 75, 75);\n"
"font: 500 20px \"Arial\";\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.note)

        self.note_2 = QFrame(self.note_wrapper)
        self.note_2.setObjectName(u"note_2")
        self.note_2.setMinimumSize(QSize(300, 0))
        self.note_2.setMaximumSize(QSize(300, 16777215))
        self.note_2.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgb(252, 252, 108), stop:1 rgb(239, 188, 20));\n"
"\n"
"border-radius: 10px;")
        self.note_2.setFrameShape(QFrame.StyledPanel)
        self.note_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.note_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_7 = QLabel(self.note_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(75, 75, 75);\n"
"font: 500 20px \"Arial\";\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.note_2)


        self.gridLayout_5.addWidget(self.note_wrapper, 0, 0, 1, 1)

        self.note_scroll.setWidget(self.note_scroll_grid)

        self.gridLayout_4.addWidget(self.note_scroll, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.Note_container)


        self.gridLayout.addWidget(self.container, 0, 0, 1, 1)

        self.course_container = QFrame(self.wrapper)
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
        self.label.setFont(font)
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
        self.verticalLayout_4 = QVBoxLayout(self.course_wrapper)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        
        # ================================================
        # ================Create courses==================
        # ================================================
        
        self.course = QFrame(self.course_wrapper)
        self.course.setObjectName(u"course")
        self.course.setMinimumSize(QSize(0, 90))
        self.course.setMaximumSize(QSize(16777215, 90))
        self.course.setLayoutDirection(Qt.LeftToRight)
        self.course.setAutoFillBackground(False)
        self.course.setStyleSheet(u"background:transparent;")
        self.course.setFrameShape(QFrame.StyledPanel)
        self.course.setFrameShadow(QFrame.Raised)

        folder_img_path = os.path.join(os.path.dirname(__file__), "../resources/icons/folder.svg")
        with open(folder_img_path, 'r') as image:
                svg_content = image.read()
                
        svg_content = svg_content.replace('fill="#cacaca"', 'fill="#dc2626"')

        self.folder_icon = QLabel(self.course)
        self.folder_icon.setMinimumSize(70, 70)
        self.folder_icon.setMaximumSize(70, 70)

        renderer = QSvgRenderer(QByteArray(svg_content.encode())) 

        pixmap = QPixmap(70, 70) 
        pixmap.fill(Qt.transparent) 

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        self.folder_icon.setPixmap(pixmap)
        self.folder_icon.setScaledContents(True)
        
        self.course_title = QLabel()
        self.course_title.setText("Bahasa Inggris")
        self.course_title.setStyleSheet("font: 20px; color: rgb(75, 75, 75);")
        
        self.session_info = QLabel()
        self.session_info.setText("Selasa, sesi 2")
        self.session_info.setStyleSheet("font: 14px; color: rgb(75, 75, 75);")
        
        self.status_dot = QFrame()
        self.status_dot.setMinimumSize(16, 16)
        self.status_dot.setMaximumSize(16, 16)
        self.status_dot.setStyleSheet("background: rgb(34, 197, 94); border-radius: 8px")
        
        self.separator = QFrame()
        self.separator.setMinimumHeight(5)
        self.separator.setStyleSheet("""
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                                        stop:0 rgb(252, 108, 108), stop:1 rgb(239, 20, 20));
        border: none;
        """)
        
        # Layouting
        self.course_layout = QVBoxLayout(self.course)
        
        self.course_top_layout = QHBoxLayout()
        self.course_top_layout.setSpacing(10)
        self.course_top_layout.addWidget(self.folder_icon)
        
        self.course_text_layout = QVBoxLayout()
        self.course_text_layout.addWidget(self.course_title)
        self.course_text_layout.addWidget(self.session_info)
        
        self.course_top_layout.addWidget(self.status_dot, alignment=Qt.AlignTop)
        self.course_top_layout.addLayout(self.course_text_layout)
        
        self.course_layout.addLayout(self.course_top_layout)
        
        self.course_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.course_layout.addWidget(self.separator)
        # ================================================
        # ================Create courses==================
        # ================================================
        
        self.verticalLayout_4.addWidget(self.course)

        self.new_course = QFrame(self.course_wrapper)
        self.new_course.setObjectName(u"new_course")
        self.new_course.setMinimumSize(QSize(0, 50))
        self.new_course.setMaximumSize(QSize(16777215, 90))
        self.new_course.setLayoutDirection(Qt.LeftToRight)
        self.new_course.setAutoFillBackground(False)
        self.new_course.setStyleSheet(u"QFrame{\n"
"border: 4px solid rgb(156, 163, 175);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
" border: 4px solid rgb(65, 225, 182);\n"
"}")
        self.new_course.setFrameShape(QFrame.StyledPanel)
        self.new_course.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.new_course)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.new_course_btn = QPushButton(self.new_course)
        self.new_course_btn.setObjectName(u"new_course_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.new_course_btn.sizePolicy().hasHeightForWidth())
        self.new_course_btn.setSizePolicy(sizePolicy4)
        self.new_course_btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(51, 65, 85);\n"
"	font: 500 20px \"Arial\";\n"
"	border: 0px;\n"
"	background: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"		color: rgb(51, 203, 198);\n"
"}")

        self.horizontalLayout_2.addWidget(self.new_course_btn)


        self.verticalLayout_4.addWidget(self.new_course)


        self.verticalLayout_5.addWidget(self.course_wrapper)


        self.gridLayout.addWidget(self.course_container, 1, 0, 1, 1)

        self.mainScroll.setWidget(self.wrapper)

        self.gridLayout_2.addWidget(self.mainScroll, 0, 0, 1, 1)

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
        self.ass_tit.setText(QCoreApplication.translate("MainWindow", u"Assigments", None))
        self.ass_text.setText(QCoreApplication.translate("MainWindow", u"UK 9 20 soal :( askolndikoajnsdijasd", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Jangan lupa hari ini ada kuis kalkulus yaawh", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Jangan lupa laprak kimia dikumpul", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Classes", None))
        self.course_wrapper.setAccessibleName("")
        self.new_course_btn.setText(QCoreApplication.translate("MainWindow", u"Tambah kelas", None))