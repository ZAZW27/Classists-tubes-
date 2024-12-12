
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller.todo import *
import json

class Todo(QFrame):
        def __init__(self, parent=None, todo_id=0, title="Undefined", id=None, ui=None, setup_todo_edit=None, setup_course=None):
                super().__init__(parent)
                
                with open(f"app/data/courses/{id}/assignment.json", "r") as file: 
                        if int(todo_id) != 0: 
                                todo_data = json.load(file)[todo_id] 
                        else: 
                                todo_data = json.load(file)
                                for keys in todo_data: new_key = str(int(keys) + 1)
                        print(todo_data.keys())
                
                self.setObjectName(u"todo_wrapper")
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
                
                self.isFinished = todo_data['isFinished']
                
                self.completeBtn = QPushButton(self.bottom)
                self.completeBtn.setObjectName("complete")

                self.verticalLayout_3.addWidget(self.completeBtn)
                
                self.deadLine = QDateEdit(self.bottom)
                self.deadLine.setObjectName(u"deadLine")
                self.deadLine.setStyleSheet(u"font: 18px;")
                
                fetchDate = todo_data.get('deadline', "0/00/0000")
                date_object = QDate.fromString(fetchDate, "d/MM/yyyy")
                
                self.deadLine.setDate(date_object) 
                self.deadLine.setDisplayFormat("dd/MM/yyyy")

                self.verticalLayout_3.addWidget(self.deadLine)

                self.todos_title = QTextEdit(self.bottom)
                self.todos_title.setObjectName(u"textEdit")
                sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
                sizePolicy2.setHorizontalStretch(0)
                sizePolicy2.setVerticalStretch(0)
                sizePolicy2.setHeightForWidth(self.todos_title.sizePolicy().hasHeightForWidth())
                self.todos_title.setSizePolicy(sizePolicy2)
                self.todos_title.setMaximumSize(QSize(16777215, 50))

                self.verticalLayout_3.addWidget(self.todos_title)


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
                self.todos_deskripsi = QTextEdit(self.frame_2)
                self.todos_deskripsi.setObjectName(u"todos_deskripsi")
                self.todos_deskripsi.setStyleSheet(u"")

                self.verticalLayout_4.addWidget(self.todos_deskripsi)


                self.horizontalLayout_4.addWidget(self.frame_2)


                self.verticalLayout.addWidget(self.body)


                self.gridLayout.addWidget(self.container, 0, 0, 1, 1)

                # self.mainScroll.setWidget(self.wrapper)
                self.wrapper = QWidget(self)
                
                self.setup_todo_edit = setup_todo_edit
                self.main_window = parent
                self.ui = ui
                self.course_id = id
                try: 
                        self.todo_id = todo_id if todo_id != 0 else new_key
                except UnboundLocalError:
                        self.todo_id = '1'
                
                self.saveEdit.clicked.connect(self.getData)
                self.deleteBtn.clicked.connect(self.deleteSignal)
                self.pushButton.clicked.connect(lambda: setup_course(self.main_window, self.ui, self.course_id))
                self.completeBtn.clicked.connect(self.finishedBtn)

                self.retranslateUi(todo_data, title, id)
                self.setButtonStyle()
                
        def retranslateUi(self, todo_data, title, id):
                self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
                self.course_title.setText(QCoreApplication.translate("MainWindow", f"{title}", None))
                self.saveEdit.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
                self.deleteBtn.setText(QCoreApplication.translate("MainWindow", u"\u24cd", None))
                self.todos_title.setText(todo_data.get('title', ""))
                self.todos_title.setStyleSheet("font: 20px; color: rgb(0, 0,0);")
                self.todos_deskripsi.setText(todo_data.get('deskripsi', ""))
                self.todos_deskripsi.setStyleSheet("font: 14px; color: rgb(0, 0,0);")

        def getData(self): 
                # course title, todo title, content
                fetch_data = [self.course_id, self.todo_id, self.todos_title.toPlainText(), self.todos_deskripsi.toPlainText(), self.deadLine.date().toString("dd/MM/yyyy"), self.completeBtn.text()]
                saveData(fetch_data)
                if self.setup_todo_edit: 
                        self.setup_todo_edit(self.main_window, self.ui, self.course_id )
        
        def deleteSignal(self): 
                reply = QMessageBox.question(
                        None,  # Parent (None means it's a standalone dialog)
                        "Confirm Deletion",
                        f"Are you sure you want to delete the course with ID {self.course_id}?",
                        QMessageBox.Yes | QMessageBox.No
                )
                
                if reply != QMessageBox.Yes :return print("Cancel penghapusan ")
                
                deleteTodo(self.course_id, self.todo_id)
                if self.setup_todo_edit: 
                        self.setup_todo_edit(self.main_window, self.ui, self.course_id )
                        
        def setButtonStyle(self): 
                self.completeBtn.setText("Complete" if self.isFinished == True else "Incomplete")
                self.completeBtn.setStyleSheet(f"""
                #complete {{
                        background-color: {'#10b981' if self.isFinished == True else '#dc2626'}; /* (#dc2626 Jika belum) (#10b981 jika benar)*/ 
                        color: white;             
                        border-radius: 15px;      
                        font-size: 16px;          
                        padding: 8px 16px;
                        font-weight: 500;
                }}
                #complete:hover {{
                        background-color: {'#16c784' if self.isFinished == True else '#ef4444'};
                }}
                #complete:pressed {{
                        background-color: {'#0d955f' if self.isFinished == True else '#b91c1c'};
                }}
                """)
        def finishedBtn(self): 
                self.isFinished =  not self.isFinished
                
                saveIsFinished(self.course_id, self.todo_id, self.isFinished)
                self.setButtonStyle()