import sys

from PyQt5.QtWidgets import QApplication
from .views import DiaryScreen, HomeScreen, LoginScreen
from .splashscreen import SplashScreen
import os

def create_app():
    app = QApplication(sys.argv)
    checkNewUser()
    splashscreen = SplashScreen()
    splashscreen.show()
    # login = LoginScreen()
    # login.show()
    sys.exit(app.exec())

def checkNewUser():
    if os.path.exists("hariku.db"):
        print("found")
    else:
        print('not found')