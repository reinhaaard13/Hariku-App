import sys

from PyQt5.QtWidgets import QApplication
from .views import DiaryScreen, HomeScreen, LoginScreen
from .splashscreen import SplashScreen

def create_app():
    app = QApplication(sys.argv)
    splashscreen = SplashScreen()
    splashscreen.show()
    # login = LoginScreen()
    # login.show()
    sys.exit(app.exec())