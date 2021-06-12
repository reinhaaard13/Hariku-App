import json
import random

from hariku.mediaplayer import MediaPlayer
from threading import Thread
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDateEdit,
    QDateTimeEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTableView,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMenuBar,
    QStatusBar,
    QSizePolicy,
    QTextEdit,
    QSpacerItem,
    QProgressBar,
    QFrame,
    QGridLayout,
    QComboBox,
    QScrollArea
)
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import Qt, QRect, QTimer
from .stylesheet import Hariku_Style
from datetime import date, datetime

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(400, 300)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setFont(Hariku_Style.get_font(6))
        self.dropShadowFrame.setStyleSheet(Hariku_Style.get_drop_shadow_stylesheet())
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")

        self.verticalLayout_2 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_pic = QLabel(self.dropShadowFrame)
        self.label_pic.setEnabled(True)
        self.label_pic.setMaximumSize(QtCore.QSize(50, 60))
        self.label_pic.setTextFormat(QtCore.Qt.AutoText)
        self.label_pic.setPixmap(QtGui.QPixmap("splashsceen\\../assets/Hariku-logo.png"))
        self.label_pic.setScaledContents(True)
        self.label_pic.setStyleSheet("QLabel { margin-top:10px }")
        self.label_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic.setObjectName("label_pic")
        self.verticalLayout_2.addWidget(self.label_pic, 0, QtCore.Qt.AlignHCenter)

        self.label_desc = QLabel(self.dropShadowFrame)
        self.label_desc.setFont(Hariku_Style.get_font(10))
        self.label_desc.setStyleSheet("")
        self.label_desc.setObjectName("label_desc")
        self.verticalLayout_2.addWidget(self.label_desc)

        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setStyleSheet(Hariku_Style.get_progressbar_stylesheet())
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setFont(Hariku_Style.get_font(8))
        self.label_loading.setStyleSheet("")
        self.label_loading.setObjectName("label_loading")
        self.verticalLayout_2.addWidget(self.label_loading)
        self.verticalLayout.addWidget(self.dropShadowFrame)
        
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_desc.setText(_translate("SplashScreen", "<center> Loading <Strong> Apps</Strong> </center>"))
        self.label_loading.setText(_translate("SplashScreen", "<center><Strong> loading .</Strong></center>"))

class RegisterScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.resize(350, 267)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setupUI()
    
    def setupUI(self):
        self.setObjectName("self")

        self.centralwidget = QWidget(self)

        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.dropShadowFrame = QFrame(self.centralwidget)
        # self.dropShadowFrame.setFont(Hariku_Style.get_font(6))
        self.dropShadowFrame.setStyleSheet(Hariku_Style.get_drop_shadow_stylesheet())
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")

        self.verticalLayout_2 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.passwordLabel = QLabel("Enter New Password")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLabel.sizePolicy().hasHeightForWidth())
        self.passwordLabel.setSizePolicy(sizePolicy)
        self.passwordLabel.setFont(Hariku_Style.get_font(16))

        self.verticalLayout_2.addWidget(self.passwordLabel, 0, Qt.AlignHCenter)

        self.pwLineEdit = QLineEdit(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwLineEdit.sizePolicy().hasHeightForWidth())
        self.pwLineEdit.setSizePolicy(sizePolicy)

        self.pwLineEdit.setFont(Hariku_Style.get_font(10))
        self.pwLineEdit.setStyleSheet(Hariku_Style.get_lineedit_stylesheet())

        self.pwLineEdit.setMaxLength(20)
        self.pwLineEdit.setFrame(True)
        self.pwLineEdit.setEchoMode(QLineEdit.Password)
        self.pwLineEdit.setAlignment(Qt.AlignCenter)
        self.pwLineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.pwLineEdit.setClearButtonEnabled(False)
        self.pwLineEdit.setFocus()

        self.verticalLayout_2.addWidget(self.pwLineEdit, 0, Qt.AlignHCenter)

        self.loginBtn = QPushButton("Register New Password",self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        self.loginBtn.setFont(Hariku_Style.get_font(10))
        self.loginBtn.setStyleSheet(Hariku_Style.get_pushbutton_stylesheet())
        self.verticalLayout_2.addWidget(self.loginBtn, 0, Qt.AlignHCenter)
        self.pwLineEdit.returnPressed.connect(self.loginBtn.click)

        self.loginBtn.clicked.connect(self.login)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 350, 21))
        self.setMenuBar(self.menubar)
    
    def login(self):
        from .database import register_user

        register_user(bytes(self.pwLineEdit.text(),encoding='utf-8'))

        dialog = LoginScreen(self)
        dialog.show()
        self.hide()

class LoginScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.resize(350, 267)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setupUI()
    
    def setupUI(self):
        self.setObjectName("self")

        self.centralwidget = QWidget(self)

        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.dropShadowFrame = QFrame(self.centralwidget)
        # self.dropShadowFrame.setFont(Hariku_Style.get_font(6))
        self.dropShadowFrame.setStyleSheet(Hariku_Style.get_drop_shadow_stylesheet())
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")

        self.verticalLayout_2 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.passwordLabel = QLabel("Enter Password")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLabel.sizePolicy().hasHeightForWidth())
        self.passwordLabel.setSizePolicy(sizePolicy)
        self.passwordLabel.setFont(Hariku_Style.get_font(16))

        self.verticalLayout_2.addWidget(self.passwordLabel, 0, Qt.AlignHCenter)

        self.pwLineEdit = QLineEdit(self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwLineEdit.sizePolicy().hasHeightForWidth())
        self.pwLineEdit.setSizePolicy(sizePolicy)
        
        self.pwLineEdit.setFont(Hariku_Style.get_font(10))
        self.pwLineEdit.setStyleSheet(Hariku_Style.get_lineedit_stylesheet())

        self.pwLineEdit.setMaxLength(20)
        self.pwLineEdit.setFrame(True)
        self.pwLineEdit.setEchoMode(QLineEdit.Password)
        self.pwLineEdit.setAlignment(Qt.AlignCenter)
        self.pwLineEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.pwLineEdit.setClearButtonEnabled(False)
        self.pwLineEdit.setFocus()

        self.verticalLayout_2.addWidget(self.pwLineEdit, 0, Qt.AlignHCenter)

        self.tryAgainLabel = None

        self.loginBtn = QPushButton("Login",self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        self.loginBtn.setFont(Hariku_Style.get_font(10))
        self.loginBtn.setStyleSheet(Hariku_Style.get_pushbutton_stylesheet())
        self.verticalLayout_2.addWidget(self.loginBtn, 0, Qt.AlignHCenter)
        self.pwLineEdit.returnPressed.connect(self.loginBtn.click)

        self.loginBtn.clicked.connect(self.login)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 350, 21))
        self.setMenuBar(self.menubar)
    
    def login(self):
        from .database import verify_user
        if verify_user(bytes(self.pwLineEdit.text(),encoding='utf-8')):
            dialog = HomeScreen(self)
            dialog.show()
            self.hide()
        else:
            if not self.tryAgainLabel:
                self.tryAgainLabel = QLabel("Wrong Password! Try again")
                self.tryAgainLabel.setFont(Hariku_Style.get_font(8))
                sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.tryAgainLabel.sizePolicy().hasHeightForWidth())
                self.tryAgainLabel.setSizePolicy(sizePolicy)
                self.tryAgainLabel.setStyleSheet("QLabel {color: red;}")
                self.verticalLayout_2.insertWidget(2, self.tryAgainLabel, alignment=Qt.AlignHCenter)
            self.pwLineEdit.setStyleSheet(Hariku_Style.get_wrong_lineedit_stylesheet())
            self.pwLineEdit.setFocus()
            self.pwLineEdit.selectAll()

from .database import deleteDiaryById, getAllDiaries, getDiaryById, getDiaryByMonth

class HomeScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Home Screen")
        self.resize(505, 461)
        self.setStyleSheet(Hariku_Style.get_window_stylesheet())
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.setupUI()
    
    def setupUI(self):
        self.setWindowIcon(Hariku_Style.getIcon())

        self.centralwidget = QWidget(self)
        self.setFocus()

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.topcenter_layout = QHBoxLayout()

        spacerItem = QSpacerItem(25, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.topcenter_layout.addItem(spacerItem)

        self.monthFilter = QDateEdit(self.centralwidget)
        self.monthFilter.setCurrentSection(QDateTimeEdit.MonthSection)
        self.monthFilter.setButtonSymbols(QSpinBox.NoButtons)
        self.monthFilter.setDate(datetime.now())
        self.monthFilter.setDisplayFormat("MMMM/yyyy")
        self.monthFilter.setFont(Hariku_Style.get_font(10))
        self.monthFilter.setStyleSheet(Hariku_Style.get_dateedit_stylesheet())
        self.monthFilter.dateChanged.connect(self.filterDiaryByMonth)
        self.topcenter_layout.addWidget(self.monthFilter)

        self.showAllBtn = QPushButton("Remove Filter", self.centralwidget)
        self.showAllBtn.setFont(Hariku_Style.get_font(8))
        self.showAllBtn.clicked.connect(self.getDiaries)
        self.showAllBtn.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(38, 160, 173)","rgb(8, 102, 112)"))
        self.topcenter_layout.addWidget(self.showAllBtn)

        spacerItem1 = QSpacerItem(25, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.topcenter_layout.addItem(spacerItem1)

        self.gridLayout.addLayout(self.topcenter_layout, 1, 0, 1, 1)

        self.bottomLayout = QHBoxLayout()

        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.bottomLayout.addItem(spacerItem2)

        self.createBtn = QPushButton("+ Add New Diary", self.centralwidget)
        self.createBtn.setFont(Hariku_Style.get_font(10))
        self.createBtn.clicked.connect(self.addNewDiary)
        self.createBtn.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(40, 186, 130)","rgb(207, 207, 188)"))
        self.bottomLayout.addWidget(self.createBtn)

        self.gridLayout.addLayout(self.bottomLayout, 4, 0, 1, 1)

        self.contentScrollArea = QScrollArea(self.centralwidget)
        self.contentScrollArea.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentScrollArea.sizePolicy().hasHeightForWidth())
        self.contentScrollArea.setSizePolicy(sizePolicy)
        self.contentScrollArea.setStyleSheet(Hariku_Style.get_scrollarea_stylesheet())
        self.contentScrollArea.setWidgetResizable(True)
        self.contentScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 487, 321))
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)

        self.getDiaries()

        # spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum , QSizePolicy.MinimumExpanding)
        # self.scrollAreaLayout.addItem(spacerItem2)

        self.contentScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.contentScrollArea, 2, 0, 1, 1)
        
        self.judul = QLabel("\nWelcome Home:)\n",self)
        self.judul.setFont(Hariku_Style.get_font(18))
        self.judul.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.judul, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

    def addNewDiary(self):
        dialog = DiaryScreen(self)
        dialog.show()
        self.hide()

    def clearScrollAreaLayout(self):
        # delete the diaries currently showind
        for i in reversed(range(self.scrollAreaLayout.count())):
            try:
                self.scrollAreaLayout.itemAt(i).widget().setParent(None)
            except AttributeError:
                self.scrollAreaLayout.removeItem(self.scrollAreaLayout.itemAt(i))

    def filterDiaryByMonth(self):
        self.clearScrollAreaLayout()

        year = self.monthFilter.date().year()
        month = self.monthFilter.date().month()

        diaries = getDiaryByMonth(year, month)

        for i, diary in enumerate(diaries):
            self.diaryItem = QWidget(self.scrollAreaWidgetContents)
            sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(self.diaryItem.sizePolicy().hasHeightForWidth())
            self.diaryItem.setSizePolicy(sizePolicy)
            self.diaryItem.setMinimumSize(QtCore.QSize(0, 50))
            self.diaryItem.setStyleSheet("background-color: rgba(227, 217, 163, 100%);\nborder-radius : 10px;")
            self.diaryItem.setObjectName("diaryItem")
            self.itemLayout = QGridLayout(self.diaryItem)

            self.contentDateLayout = QVBoxLayout()
            self.contentDateLayout.setObjectName("contentDateLayout")

            self.content = QLabel(self.truncateString(diary.content), self.diaryItem)
            self.content.setFont(Hariku_Style.get_font(10))
            self.contentDateLayout.addWidget(self.content)

            self.date = QLabel(diary.date.strftime("%d %B %Y") + diary.time.strftime("  %I:%M %p"), self.diaryItem)
            self.date.setFont(Hariku_Style.get_font(8))
            self.contentDateLayout.addWidget(self.date)

            self.itemLayout.addLayout(self.contentDateLayout, 0, 0, 1, 1)

            self.buttons.append(i)
            self.buttons[i] = [QPushButton("⋗", self.diaryItem),QPushButton("×", self.diaryItem)]

            self.buttons[i][0].clicked.connect(lambda checked, i=diary.diary_id: self.viewDiaryById(i))
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.buttons[i][0].sizePolicy().hasHeightForWidth())
            self.buttons[i][0].setSizePolicy(sizePolicy)
            self.buttons[i][0].setFont(Hariku_Style.get_font(9))
            self.buttons[i][0].setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(145, 133, 63)","rgb(235, 224, 157)"))
            self.itemLayout.addWidget(self.buttons[i][0], 0, 1, 1, 1)

            # self.deleteBtn = QPushButton("×", self.diaryItem)
            self.buttons[i][1].clicked.connect(lambda checked, i=diary.diary_id: self.deleteDiaryById(i))
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.buttons[i][1].sizePolicy().hasHeightForWidth())
            self.buttons[i][1].setSizePolicy(sizePolicy)
            self.buttons[i][1].setFont(Hariku_Style.get_font(9))
            self.buttons[i][1].setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(145, 63, 63)","rgb(235, 157, 157)"))
            self.itemLayout.addWidget(self.buttons[i][1], 0, 2, 1, 1)

            self.scrollAreaLayout.addWidget(self.diaryItem, alignment=QtCore.Qt.AlignTop)
        
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum , QSizePolicy.MinimumExpanding)
        self.scrollAreaLayout.addItem(spacerItem2)


    def getDiaries(self):
        diaries = getAllDiaries()

        self.monthFilter.setDate(datetime.now())
        self.clearScrollAreaLayout()

        self.buttons = []

        for i, diary in enumerate(diaries):
            self.diaryItem = QWidget(self.scrollAreaWidgetContents)
            sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(self.diaryItem.sizePolicy().hasHeightForWidth())
            self.diaryItem.setSizePolicy(sizePolicy)
            self.diaryItem.setMinimumSize(QtCore.QSize(0, 50))
            self.diaryItem.setStyleSheet("background-color: rgba(227, 217, 163, 100%);\nborder-radius : 10px;")
            self.diaryItem.setObjectName("diaryItem")
            self.itemLayout = QGridLayout(self.diaryItem)

            self.contentDateLayout = QVBoxLayout()
            self.contentDateLayout.setObjectName("contentDateLayout")

            self.content = QLabel(self.truncateString(diary.content), self.diaryItem)
            self.content.setFont(Hariku_Style.get_font(10))
            self.contentDateLayout.addWidget(self.content)

            self.date = QLabel(diary.date.strftime("%d %B %Y") + diary.time.strftime("  %I:%M %p"), self.diaryItem)
            self.date.setFont(Hariku_Style.get_font(8))
            self.contentDateLayout.addWidget(self.date)

            self.itemLayout.addLayout(self.contentDateLayout, 0, 0, 1, 1)

            self.buttons.append(i)
            self.buttons[i] = [QPushButton("⋗", self.diaryItem),QPushButton("×", self.diaryItem)]

            self.buttons[i][0].clicked.connect(lambda checked, i=diary.diary_id: self.viewDiaryById(i))
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.buttons[i][0].sizePolicy().hasHeightForWidth())
            self.buttons[i][0].setSizePolicy(sizePolicy)
            self.buttons[i][0].setFont(Hariku_Style.get_font(9))
            self.buttons[i][0].setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(145, 133, 63)","rgb(235, 224, 157)"))
            self.itemLayout.addWidget(self.buttons[i][0], 0, 1, 1, 1)

            # self.deleteBtn = QPushButton("×", self.diaryItem)
            self.buttons[i][1].clicked.connect(lambda checked, i=diary.diary_id: self.deleteDiaryById(i))
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.buttons[i][1].sizePolicy().hasHeightForWidth())
            self.buttons[i][1].setSizePolicy(sizePolicy)
            self.buttons[i][1].setFont(Hariku_Style.get_font(9))
            self.buttons[i][1].setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(145, 63, 63)","rgb(235, 157, 157)"))
            self.itemLayout.addWidget(self.buttons[i][1], 0, 2, 1, 1)

            self.scrollAreaLayout.addWidget(self.diaryItem, alignment=QtCore.Qt.AlignTop)

        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum , QSizePolicy.MinimumExpanding)
        self.scrollAreaLayout.addItem(spacerItem2)


    def truncateString(self, string):
        try:
            string = string.replace('\n',' ')
            return string[:45] + '...'
        except IndexError:
            return string

    def viewDiaryById(self, id):
        dialog = DiaryScreen(self, edit=False, id=id)
        dialog.show()
        self.hide()

    def deleteDiaryById(self, id):
        deleteDiaryById(id)
        self.clearScrollAreaLayout()
        self.getDiaries()

class DiaryScreen(QMainWindow):
    
    def __init__(self, parent=None, edit=True, id=None):
        super().__init__(parent)
        self.setWindowTitle("Add Diary")
        self.resize(642, 379)
        self.setStyleSheet(Hariku_Style.get_window_stylesheet())
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.timestamp = datetime.now()

        self.setupUI(edit, id)

    def setupUI(self, edit=True, id=None):
        self.setWindowIcon(Hariku_Style.getIcon())

        self.centralwidget = QWidget(self)

        self.horizontalLayout = QHBoxLayout(self.centralwidget)

        self.SideBar = QVBoxLayout()

        self.date = QLabel(self.timestamp.strftime("%A, %B %e, %Y"), self)
        self.date.setFont(Hariku_Style.get_font(14))
        self.SideBar.addWidget(self.date)

        self.clock = QLabel(self.timestamp.strftime("%I:%M:%S %p"), self)
        self.clock.setFont(Hariku_Style.get_font(20))
        self.SideBar.addWidget(self.clock)

        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.SideBar.addItem(spacerItem)

        if edit == True:
            self.randomBtn = QPushButton("Generate Random Question", self)
            self.randomBtn.setFont(Hariku_Style.get_font(10))
            self.randomBtn.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(24, 88, 191)","rgb(207, 207, 188)"))
            self.randomBtn.clicked.connect(self.generateRandomQuestion)
            self.SideBar.addWidget(self.randomBtn)

        # Create Music Player
        self.hlayout_music = QHBoxLayout()
        self.hlayout_music.setObjectName("hlayout_music")

        # Instantiate Media Player Object
        self.player = MediaPlayer()

        self.hlayout_music = QHBoxLayout()
        self.hlayout_music.setObjectName("hlayout_music")

        self.vl_down = QPushButton("-")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.vl_down.setSizePolicy(sizePolicy)
        self.vl_down.setMinimumSize(QtCore.QSize(20, 0))
        self.vl_down.setFont(Hariku_Style.get_font(10))
        self.vl_down.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(185, 150, 24)","rgb(207, 207, 188)"))
        self.vl_down.setObjectName("vl_down")
        self.vl_down.clicked.connect(lambda:self.player.changeVolumeBy(-5))
        self.hlayout_music.addWidget(self.vl_down)

        self.playBtn = QPushButton("Play Music")
        self.playBtn.setFont(Hariku_Style.get_font(10))
        self.playBtn.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(185, 150, 24)","rgb(207, 207, 188)"))
        self.playBtn.setObjectName("playBtn")
        self.playBtn.clicked.connect(self.togglePlay)
        self.hlayout_music.addWidget(self.playBtn)

        self.vl_up = QPushButton("+")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.vl_up.setSizePolicy(sizePolicy)
        self.vl_up.setMinimumSize(QtCore.QSize(20, 0))
        self.vl_up.setFont(Hariku_Style.get_font(10))
        self.vl_up.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(185, 150, 24)","rgb(207, 207, 188)"))
        self.vl_up.setObjectName("vl_up")
        self.vl_up.clicked.connect(lambda:self.player.changeVolumeBy(5))
        self.hlayout_music.addWidget(self.vl_up)
        self.SideBar.addLayout(self.hlayout_music)

        self.hlayout_save = QHBoxLayout()
        self.hlayout_save.setObjectName("hlayout_save")

        self.exitBtn = QPushButton("Exit", self)
        self.exitBtn.setFont(Hariku_Style.get_font(8))
        self.exitBtn.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet_invert("rgb(255, 57, 46)","rgba(255, 57, 46, 25%)"))
        self.hlayout_save.addWidget(self.exitBtn)
        self.exitBtn.clicked.connect(self.exit)

        if edit == True:
            self.saveBtn = QPushButton("Save Diary", self)
            self.saveBtn.setFont(Hariku_Style.get_font(10))
            self.saveBtn.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(40, 186, 130)","rgb(207, 207, 188)"))
            self.saveBtn.clicked.connect(self.saveDiary)
            self.hlayout_save.addWidget(self.saveBtn)

        self.SideBar.addLayout(self.hlayout_save)
        self.horizontalLayout.addLayout(self.SideBar)

        self.diaryArea = QTextEdit(self)
        self.diaryArea.setFont(Hariku_Style.get_font(10))
        self.diaryArea.setStyleSheet(Hariku_Style.get_diary_textarea_stylesheet())
        self.diaryArea.setFocus()
        self.diaryArea.setReadOnly(True) if edit == False else self.diaryArea.setReadOnly(False)
        self.horizontalLayout.addWidget(self.diaryArea)
        
        self.setCentralWidget(self.centralwidget)

        if edit == True:
            # creating a timer object
            # adding action to timer
            # update the timer every second
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start(1000)

            # Timer for refreshing mood score
            self.mood_timer = QTimer(self)
            self.mood_timer.timeout.connect(lambda: self.player.reviewMood(self.diaryArea.toPlainText()))
            self.mood_timer.start(10000)

        elif edit == False:
            self.viewPrefilledDiary(id)

    def showTime(self):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        self.clock.setText(current_time)
    
    def togglePlay(self):
        self.playBtn.setText(self.player.togglePlay())

    def exit(self):
        try:
            self.player.stop()
            self.mood_timer.stop()
        except AttributeError:
            pass
        dialog = HomeScreen(self)
        dialog.show()
        self.hide()

    def saveDiary(self):
        from .database import addDiary
        if not self.diaryArea.toPlainText():
            return
        date = datetime.now().date()
        time = datetime.now().time()
        content = self.diaryArea.toPlainText()
        mood_score = self.player.getMoodScore()
        addDiary(date, time, content, mood_score)
        self.exit()

    def generateRandomQuestion(self):
        with open('hariku/questions.json',) as question:
            choices = json.load(question)
            question = random.choice(choices['questions'])
            self.diaryArea.insertPlainText(f" [ {question} ] \n")

    def viewPrefilledDiary(self, id):
        diary = getDiaryById(id)
        self.clock.setText(diary.time.strftime("%I:%M:%S %p"))
        self.date.setText(diary.date.strftime("%A, %B %e, %Y"))
        self.diaryArea.setText(diary.content)