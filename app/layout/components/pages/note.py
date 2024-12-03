
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Note(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
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

        self.delete_2 = QPushButton(self.frame)
        self.delete_2.setObjectName(u"delete_2")
        sizePolicy1.setHeightForWidth(self.delete_2.sizePolicy().hasHeightForWidth())
        self.delete_2.setSizePolicy(sizePolicy1)
        self.delete_2.setMinimumSize(QSize(50, 50))
        self.delete_2.setStyleSheet(u"color: rgb(255,0,0);\n"
"font: 40px;")

        self.horizontalLayout_2.addWidget(self.delete_2)


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

        self.verticalLayout_3.addWidget(self.deadLine)

        self.textEdit = QTextEdit(self.bottom)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_3.addWidget(self.textEdit)


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
        self.textEdit_2 = QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.textEdit_2)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.body)


        self.gridLayout.addWidget(self.container, 0, 0, 1, 1)

        # self.mainScroll.setWidget(self.wrapper)
        self.wrapper = QWidget(self)

        # self.gridLayout_2.addWidget(self.mainScroll, 0, 0, 1, 1)

        # MainWindow.setCentralWidget(self.centralwidget)
        # self.statusBar = QStatusBar(MainWindow)
        # self.statusBar.setObjectName(u"statusBar")
        # MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi()

        # QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.course_title.setText(QCoreApplication.translate("MainWindow", u"KIMIA", None))
        self.saveEdit.setText(QCoreApplication.translate("MainWindow", u"\u2713", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"\u24cd", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Jangan lupa ada laprak yang belum dikumpul nanti, apalagi nanti ada yang kak chenita wahyu</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oh, whoa-whoa, oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Judas, Judas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oh-oh-oh-oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Judas, Judas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Juda-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Gaga</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Juda-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Gaga</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><s"
                        "pan style=\" font-size:12pt;\">When he calls to me, I am ready</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'll wash his feet with my hair if he needs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Forgive him when his tongue lies through his brain</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Even after three times, he betrays me</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ah-ah, ah-ah-ah-ah, ah-ah, ah-ah-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'll bring him down, bring him down, down</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ah-ah, ah-ah-ah-ah, ah-ah, ah-ah-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">A king with no crown, king with no crown</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm just a Holy Fool, oh, baby, it's so cruel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">But I'm still in love with Judas, baby</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm just a Holy Fool, oh, baby, it's so cruel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">But I'm still in love with Judas, baby</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oh, whoa-whoa, oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Judas, Judas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oh-oh-oh-oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Judas, Judas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Juda-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Gaga</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I couldn't love a man so purely</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Even prophets forgave his goofy way</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0"
                        "px;\"><span style=\" font-size:12pt;\">I've learned love is like a brick, you can</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Build a house or sink a dead body</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ah-ah, ah-ah-ah-ah, ah-ah, ah-ah-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'll bring him down, bring him down, down</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ah-ah, ah-ah-ah-ah, ah-ah, ah-ah-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-size:12pt;\">A king with no crown, king with no crown</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm just a Holy Fool, oh, baby, it's so cruel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">But I'm still in love with Judas, baby</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm just a Holy Fool, oh, baby, it's so cruel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">But I'm still in love with Judas, baby</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oh, whoa-whoa, oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Juda-as, Juda-as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oh-oh-oh-oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Juda-as, Juda-as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ew</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-size:12pt;\">In the most Biblical sense, I am beyond repentance</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Fame hooker, prostitute, wench vomits her mind</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">But in the cultural sense, I just speak in future tense</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, kiss me if offensed, or wear ear condom next time</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I wanna love you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-"
                        "indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">But something's pulling me away from you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Jesus is my virtue</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">And Judas is the demon I cling to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I cling to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Just a Holy Fool, oh, baby, it's so cruel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-size:12pt;\">But I'm still in love with Judas, baby</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm just a Holy Fool, oh, baby, it's so cruel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">But I'm still in love with Judas, baby</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Oh, whoa-whoa, oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Judas, Judas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span sty"
                        "le=\" font-size:12pt;\">Oh-oh-oh-oh-oh</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">I'm in love with Judas, Judas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Juda-ah-ah</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Judas, Juda-ah-ah, Judas, Gaga</span></p></body></html>", None))
    # retranslateUi

