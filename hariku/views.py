import json
import random
from hariku.mediaplayer import MediaPlayer
from threading import Thread
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
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
    QFrame
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

        self.loginBtn = QPushButton("Save Password",self.centralwidget)
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
            self.pwLineEdit.setStyleSheet(Hariku_Style.get_wrong_lineedit_stylesheet())
            self.pwLineEdit.setFocus()
            self.pwLineEdit.selectAll()

class HomeScreen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Home Screen")
        self.resize(250, 150)
        self.setStyleSheet(Hariku_Style.get_window_stylesheet())
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.setupUI()
    
    def setupUI(self):
        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.newBtn = QPushButton("New Diary",self.centralwidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newBtn.sizePolicy().hasHeightForWidth())
        self.newBtn.setSizePolicy(sizePolicy)

        self.newBtn.setFont(Hariku_Style.get_font(10))

        self.newBtn.setStyleSheet(Hariku_Style.get_pushbutton_stylesheet())
        self.verticalLayout.addWidget(self.newBtn, 0, Qt.AlignHCenter)

        self.newBtn.clicked.connect(self.addNewDiary)

        self.setCentralWidget(self.centralwidget)

    def addNewDiary(self):
        dialog = DiaryScreen(self)
        dialog.show()
        self.hide()

from .moodselect import Mood

class DiaryScreen(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Diary")
        self.resize(642, 379)
        self.setStyleSheet(Hariku_Style.get_window_stylesheet())
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.timestamp = datetime.now()

        self.setupUI()

    def setupUI(self):
        self.centralwidget = QWidget(self)

        self.horizontalLayout = QHBoxLayout(self.centralwidget)

        self.SideBar = QVBoxLayout()

        self.date = QLabel(self.timestamp.strftime("%A, %B %e, %Y"), self)
        self.date.setFont(Hariku_Style.get_font(14))
        self.SideBar.addWidget(self.date)

        self.clock = QLabel(self.timestamp.strftime("%I:%M:%S %p"), self)
        self.clock.setFont(Hariku_Style.get_font(20))
        self.SideBar.addWidget(self.clock)

        # creating a timer object
        # adding action to timer
        # update the timer every second
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.mood = Mood()

        # Timer for refreshing mood score
        self.mood_timer = QTimer(self)
        self.mood_timer.timeout.connect(lambda: self.mood.count_mood(self.diaryArea.toPlainText()))
        self.mood_timer.start(5000)

        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.SideBar.addItem(spacerItem)

        self.randomBtn = QPushButton("Generate Random Question", self)
        self.randomBtn.setFont(Hariku_Style.get_font(10))
        # rgb(24, 88, 191)
        # rgb(207, 207, 188)
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

        self.saveBtn = QPushButton("Save Diary", self)
        self.saveBtn.setFont(Hariku_Style.get_font(10))
        self.saveBtn.setStyleSheet(Hariku_Style.get_moodBtn_stylesheet("rgb(40, 186, 130)","rgb(207, 207, 188)"))
        self.hlayout_save.addWidget(self.saveBtn)

        self.SideBar.addLayout(self.hlayout_save)
        self.horizontalLayout.addLayout(self.SideBar)

        self.diaryArea = QTextEdit(self)
        self.diaryArea.setFont(Hariku_Style.get_font(10))
        self.diaryArea.setStyleSheet(Hariku_Style.get_diary_textarea_stylesheet())
        self.horizontalLayout.addWidget(self.diaryArea)
        
        self.setCentralWidget(self.centralwidget)

    def showTime(self):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        self.clock.setText(current_time)
    
    def togglePlay(self):
        self.playBtn.setText(self.player.togglePlay())

    def exit(self):
        self.player.stop()
        self.mood_timer.stop()
        dialog = HomeScreen(self)
        dialog.show()
        self.hide()

    def generateRandomQuestion(self):
        with open('hariku/questions.json',) as question:
            choices = json.load(question)
            question = random.choice(choices['questions'])
            self.diaryArea.insertPlainText(f" [ {question} ] \n")