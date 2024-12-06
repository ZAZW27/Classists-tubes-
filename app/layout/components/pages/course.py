#
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from controller.course import *

class Course(QFrame):
    def __init__(self, parent=None, course_id=None):
        super().__init__(parent)
        
        self.setObjectName(u"wrapper")
        self.setStyleSheet("color: rgb(0,0,0);")
        self.setGeometry(QRect(0, 0, 700, 632))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.del_btn = QPushButton(self.frame)
        self.del_btn.setObjectName(u"del_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_btn.sizePolicy().hasHeightForWidth())
        self.del_btn.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.del_btn.setIcon(icon)

        self.gridLayout_5.addWidget(self.del_btn, 0, 3, 1, 1)

        self.course_title_lbl = QLabel(self.frame)
        self.course_title_lbl.setObjectName(u"course_title_lbl")
        self.course_title_lbl.setMinimumSize(QSize(0, 150))
        self.course_title_lbl.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout_5.addWidget(self.course_title_lbl, 1, 0, 1, 4)

        self.return_btn = QPushButton(self.frame)
        self.return_btn.setObjectName(u"return_btn")
        sizePolicy.setHeightForWidth(self.return_btn.sizePolicy().hasHeightForWidth())
        self.return_btn.setSizePolicy(sizePolicy)
        self.return_btn.setMinimumSize(QSize(0, 25))
        self.return_btn.setStyleSheet(u"text-align:left;")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.return_btn.setIcon(icon1)

        self.gridLayout_5.addWidget(self.return_btn, 0, 0, 1, 1)

        self.edit_btn = QPushButton(self.frame)
        self.edit_btn.setObjectName(u"edit_btn")
        sizePolicy.setHeightForWidth(self.edit_btn.sizePolicy().hasHeightForWidth())
        self.edit_btn.setSizePolicy(sizePolicy)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.edit_btn.setIcon(icon2)

        self.gridLayout_5.addWidget(self.edit_btn, 0, 2, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.classroom_lbl = QLabel(self.frame_5)
        self.classroom_lbl.setObjectName(u"classroom_lbl")
        self.classroom_lbl.setMinimumSize(QSize(0, 50))
        self.classroom_lbl.setMaximumSize(QSize(16777215, 50))
        self.classroom_lbl.setStyleSheet(u"")
        self.classroom_lbl.setScaledContents(True)
        self.classroom_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.classroom_lbl.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.classroom_lbl)

        self.session_lbl = QLabel(self.frame_5)
        self.session_lbl.setObjectName(u"session_lbl")
        self.session_lbl.setMinimumSize(QSize(0, 50))
        self.session_lbl.setMaximumSize(QSize(16777215, 50))
        self.session_lbl.setStyleSheet(u"")
        self.session_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.session_lbl)

        self.gridLayout_5.addWidget(self.frame_5, 2, 0, 1, 4)

        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(217, 231, 255);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.todo_title_lbl = QLabel(self.frame_4)
        self.todo_title_lbl.setObjectName(u"todo_title_lbl")

        self.horizontalLayout.addWidget(self.todo_title_lbl)

        self.add_todo_btn = QPushButton(self.frame_4)
        self.add_todo_btn.setObjectName(u"add_todo_btn")
        self.add_todo_btn.setStyleSheet(u"text-align:right;")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.add_todo_btn.setIcon(icon3)

        self.horizontalLayout.addWidget(self.add_todo_btn)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.todo_list_frm = QFrame(self.frame_3)
        self.todo_list_frm.setObjectName(u"todo_list_frm")
        self.todo_list_frm.setFrameShape(QFrame.Shape.StyledPanel)
        self.todo_list_frm.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.todo_list_frm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.todo_list_lyt = QVBoxLayout()
        self.todo_list_lyt.setObjectName(u"todo_list_lyt")

        self.gridLayout_3.addLayout(self.todo_list_lyt, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.todo_list_frm)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 243, 189);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.note_title_btn = QLabel(self.frame_6)
        self.note_title_btn.setObjectName(u"note_title_btn")

        self.horizontalLayout_2.addWidget(self.note_title_btn)

        self.add_note_btn = QPushButton(self.frame_6)
        self.add_note_btn.setObjectName(u"add_note_btn")
        self.add_note_btn.setStyleSheet(u"text-align:right;")
        self.add_note_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.add_note_btn)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.note_list_frm = QFrame(self.frame_2)
        self.note_list_frm.setObjectName(u"note_list_frm")
        self.note_list_frm.setFrameShape(QFrame.Shape.StyledPanel)
        self.note_list_frm.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.note_list_frm)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.note_list_lyt = QVBoxLayout()
        self.note_list_lyt.setObjectName(u"note_list_lyt")

        self.gridLayout_4.addLayout(self.note_list_lyt, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.note_list_frm)


        self.verticalLayout.addWidget(self.frame_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        # self.mainScroll.setWidget(self)

        # self.gridLayout_2.addWidget(self.mainScroll, 0, 0, 1, 1)

        # MainWindow.setCentralWidget(self.centralwidget)
        # self.statusBar = QStatusBar(MainWindow)
        # self.statusBar.setObjectName(u"statusBar")
        # MainWindow.setStatusBar(self.statusBar)
        self.add_note_btn.clicked.connect(self.add_new_note)   

        self.retranslateUi()

        # QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self):
        print("ready")
        # MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Course - Dashboard", None))
        self.del_btn.setText(QCoreApplication.translate("MainWindow", u"Hapus Course", None))
        self.course_title_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Course Name</span></p></body></html>", None))
        self.return_btn.setText(QCoreApplication.translate("MainWindow", u"Kembali", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit Course", None))
        self.classroom_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Ruang Kelas:</span></p></body></html>", None))
        self.session_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Sesi:</span></p></body></html>", None))
        self.todo_title_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">To-Dos</span></p></body></html>", None))
        self.add_todo_btn.setText(QCoreApplication.translate("MainWindow", u"Tambah Tugas", None))
        self.note_title_btn.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Notes</span></p></body></html>", None))
        self.add_note_btn.setText(QCoreApplication.translate("MainWindow", u"Tambah Catatan", None))
    # retranslateUi
    
    def add_new_note(self): 
        # print("aosdnasidiansjdanskdnkadnklasn andi nuafal")
        show_new_note_form()