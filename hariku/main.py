from hariku.views import LoginScreen
import sys

from PyQt5.QtWidgets import QApplication
from .views import DiaryScreen, HomeScreen, LoginScreen, MoodScreen

def main():
    app = QApplication(sys.argv)
    
    login = LoginScreen()
    login.show()
    sys.exit(app.exec())