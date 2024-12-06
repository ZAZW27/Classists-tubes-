
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller.notes import *
import json

class Note(QFrame):
        def __init__(self, parent=None, notes_id=None, title="Undefined", id=None, ui=None, setup_note_edit=None):
                super().__init__(parent)
                print(f"notes id {notes_id}")
                print(f"Folder id {id}")
                with open(f"app/data/courses/{id}/note.json", "r") as file: 
                        notes_data = json.load(file)[notes_id]
                
                self.setObjectName(u"note_wrapper")
                self.setGeometry(0, 0, 679, 1037)
                self.gridLayout = QGridLayout(self)
                self.gridLayout.setObjectName(u"gridLayout")
                self.gridLayout.setHorizontalSpacing(0)
                self.gridLayout.setVerticalSpacing(12)
                self.gridLayout.setContentsMargins(0, 0, 0, 0)
                self.container = QFrame(self)
                self.container.setObjectName(u"container")
                self.container.setFrameShape(QFrame.StyledPanel)
                self.container.setFrameShadow(QFrame.Raised)
                self.container.setStyleSheet("color: rgb(0,0,0);")
                self.verticalLayout = QVBoxLayout(self.container)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
                self.header = QFrame(self.container)
                self.header.setObjectName(u"header")
                sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
                self.header.setSizePolicy(sizePolicy)
                self.header.setStyleSheet(u"")
                self.header.setFrameShape(QFrame.StyledPanel)
                self.header.setFrameShadow(QFrame.Raised)
                self.verticalLayout_2 = QVBoxLayout(self.header)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.verticalLayout_2.setContentsMargins(-1, 6, -1, 0)
                self.top = QFrame(self.header)
                self.top.setObjectName(u"top")
                sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
                self.top.setSizePolicy(sizePolicy)
                self.top.setStyleSheet(u"background: rgb(255, 255, 255)")
                self.top.setFrameShape(QFrame.StyledPanel)
                self.top.setFrameShadow(QFrame.Raised)
                self.horizontalLayout = QHBoxLayout(self.top)
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.pushButton = QPushButton(self.top)
                self.pushButton.setObjectName(u"pushButton")
                sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
                self.pushButton.setSizePolicy(sizePolicy1)
                self.pushButton.setStyleSheet(u"font: 40px;")

                self.horizontalLayout.addWidget(self.pushButton)

                self.course_title = QLabel(self.top)
                self.course_title.setObjectName(u"course_title")
                self.course_title.setStyleSheet(u"font: 40px;")
                self.course_title.setAlignment(Qt.AlignCenter)

                self.horizontalLayout.addWidget(self.course_title)

                self.frame = QFrame(self.top)
                self.frame.setObjectName(u"frame")
                self.frame.setFrameShape(QFrame.StyledPanel)
                self.frame.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_2 = QHBoxLayout(self.frame)
                self.horizontalLayout_2.setSpacing(25)
                self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
                self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
                self.saveEdit = QPushButton(self.frame)
                self.saveEdit.setObjectName(u"saveEdit")
                sizePolicy1.setHeightForWidth(self.saveEdit.sizePolicy().hasHeightForWidth())
                self.saveEdit.setSizePolicy(sizePolicy1)
                self.saveEdit.setMinimumSize(QSize(20, 20))
                self.saveEdit.setMaximumSize(QSize(40, 40))
                self.saveEdit.setStyleSheet(u"color: rgb(0,255,0);\n"
        "font: 40px; border: 2px solid rgb(0,200,120); border-radius: 17px;")

                self.horizontalLayout_2.addWidget(self.saveEdit)
                
                self.deleteBtn = QPushButton(self.frame)
                self.deleteBtn.setObjectName(u"deleteBtn")
                sizePolicy1.setHeightForWidth(self.deleteBtn.sizePolicy().hasHeightForWidth())
                self.deleteBtn.setSizePolicy(sizePolicy1)
                self.deleteBtn.setMinimumSize(QSize(50, 50))
                self.deleteBtn.setStyleSheet(u"color: rgb(255,0,0);\n"
        "font: 40px;")

                self.horizontalLayout_2.addWidget(self.deleteBtn)


                self.horizontalLayout.addWidget(self.frame)


                self.verticalLayout_2.addWidget(self.top)

                self.bottom = QFrame(self.header)
                self.bottom.setObjectName(u"bottom")
                sizePolicy.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())
                self.bottom.setSizePolicy(sizePolicy)
                self.bottom.setStyleSheet(u"background: rgb(255,255,255);")
                self.bottom.setFrameShape(QFrame.StyledPanel)
                self.bottom.setFrameShadow(QFrame.Raised)
                self.verticalLayout_3 = QVBoxLayout(self.bottom)
                self.verticalLayout_3.setObjectName(u"verticalLayout_3")
                self.deadLine = QDateEdit(self.bottom)
                self.deadLine.setObjectName(u"deadLine")
                self.deadLine.setStyleSheet(u"font: 18px;")
                
                fetchDate = notes_data['created_at']
                date_object = QDate.fromString(fetchDate, "d/MM/yyyy")
                
                self.deadLine.setDate(date_object) 
                self.deadLine.setDisplayFormat("dd/MM/yyyy")


                self.verticalLayout_3.addWidget(self.deadLine)

                self.notes_title = QTextEdit(self.bottom)
                self.notes_title.setObjectName(u"textEdit")
                sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
                sizePolicy2.setHorizontalStretch(0)
                sizePolicy2.setVerticalStretch(0)
                sizePolicy2.setHeightForWidth(self.notes_title.sizePolicy().hasHeightForWidth())
                self.notes_title.setSizePolicy(sizePolicy2)
                self.notes_title.setMaximumSize(QSize(16777215, 50))

                self.verticalLayout_3.addWidget(self.notes_title)


                self.verticalLayout_2.addWidget(self.bottom)


                self.verticalLayout.addWidget(self.header)

                self.body = QFrame(self.container)
                self.body.setObjectName(u"body")
                self.body.setStyleSheet(u"")
                self.body.setFrameShape(QFrame.StyledPanel)
                self.body.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_4 = QHBoxLayout(self.body)
                self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
                self.frame_2 = QFrame(self.body)
                self.frame_2.setObjectName(u"frame_2")
                self.frame_2.setStyleSheet(u"background: rgb(255,255,255);")
                self.frame_2.setFrameShape(QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QFrame.Raised)
                self.verticalLayout_4 = QVBoxLayout(self.frame_2)
                self.verticalLayout_4.setObjectName(u"verticalLayout_4")
                self.notes_deskripsi = QTextEdit(self.frame_2)
                self.notes_deskripsi.setObjectName(u"notes_deskripsi")
                self.notes_deskripsi.setStyleSheet(u"")

                self.verticalLayout_4.addWidget(self.notes_deskripsi)


                self.horizontalLayout_4.addWidget(self.frame_2)


                self.verticalLayout.addWidget(self.body)


                self.gridLayout.addWidget(self.container, 0, 0, 1, 1)

                # self.mainScroll.setWidget(self.wrapper)
                self.wrapper = QWidget(self)
                
                self.setup_note_edit = setup_note_edit
                self.main_window = parent
                self.ui = ui
                self.course_id = id
                self.notes_id = notes_id
                
                self.saveEdit.clicked.connect(self.getData)
                self.deleteBtn.clicked.connect(self.deleteSignal)

                self.retranslateUi(notes_data, title, id)
                
        def retranslateUi(self, notes_data, title, id):
                self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
                self.course_title.setText(QCoreApplication.translate("MainWindow", f"{title}", None))
                self.saveEdit.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
                self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"\u24cd", None))
                self.notes_title.setText(notes_data['title'])
                self.notes_title.setStyleSheet("font: 20px; color: rgb(0, 0,0);")
                self.notes_deskripsi.setText(notes_data['deskripsi'])
                self.notes_deskripsi.setStyleSheet("font: 14px; color: rgb(0, 0,0);")

        def getData(self): 
                # course title, note title, content
                fecth_data = [self.course_id, self.notes_id, self.notes_title.toPlainText(), self.notes_deskripsi.toPlainText(), self.deadLine.date().toString("dd/MM/yyyy")]
                saveData(fecth_data)
        
        def deleteSignal(self): 
                deleteNote(self.course_id, self.notes_id)
                if self.setup_note_edit: 
                        self.setup_note_edit(self.main_window, self.ui, self.course_id,self.notes_id )