from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

## ==> SPLASH SCREEN
from .views import Ui_SplashScreen

counter = 0

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # TIMER IN MILLISECONDS
        self.timer.start(10)

        # Initial Text
        self.ui.label_desc.setText("<center> Loading <Strong> Apps</Strong> </center>")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_desc.setText("<center> Loading <Strong> Databases</Strong> </center>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_desc.setText("<center> Loading <Strong> UI</Strong> </center>"))
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_loading.setText("<center><Strong>loading . .</Strong></center>"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText("<center><Strong>loading . . .</Strong></center>"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.label_loading.setText("<center><Strong>loading .</Strong></center>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("<center><Strong>loading . .</Strong></center>"))

        # self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            import os
            if os.path.exists("hariku.db"):
                from .views import LoginScreen
                self.main = LoginScreen()
                self.main.show()
            else:
                from .views import RegisterScreen
                self.main = RegisterScreen()
                self.main.show()

            # CLOSE SPLASH SCREEN
            self.hide()

        # INCREASE COUNTER
        counter += 1