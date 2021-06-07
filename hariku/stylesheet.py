from PyQt5.QtGui import QFont

class Hariku_Style:

    def get_drop_shadow_stylesheet():
        return """
            QFrame{
                background-color: rgb(240, 240, 217);
                color:rgb(0, 0, 0);
                border-radius: 25px;
            }
        """

    def get_progressbar_stylesheet():
        return """
            QProgressBar{
                background-color: rgb(227, 227, 206);
                color:rgb(0,0,0);
                border-style: none;
                border-color:rgb(40, 186, 130);
                border-radius: 10px;
                text-align: center;
                margin: 0 10px;
            }
            QProgressBar::chunk {
                border-radius:10px;
                background-color: qlineargradient(spread:pad, x1:0, y1:0.545, x2:1, y2:0.557, stop:0 rgba(24, 88, 191, 255), stop:1 rgba(40, 186, 130, 255));
            }
            """

    def get_window_stylesheet():
        return """
        background-color: rgb(240, 240, 217);
        """

    def get_lineedit_stylesheet():
        return """
            QLineEdit{
                width: 205px;
                height: 25px;
                padding:10px;
                border: 0px;
                border-radius: 10px;
                background-color:rgb(227, 227, 206);
            }
            QLineEdit:hover{
                background-color:rgb(211, 211, 191);
            }
            QLineEdit:focus{
                border: 1px solid rgb(31, 117, 253);
                background-color:rgb(211, 211, 191);
            }
        """

    def get_wrong_lineedit_stylesheet():
        return """
            QLineEdit{
                width: 205px;
                height: 25px;
                padding:10px;
                border: 1px solid rgb(102, 0, 0);
                border-radius: 10px;
                background-color:rgb(224, 114, 114);
            }
            QLineEdit:hover{
                background-color:rgb(219, 134, 134);
            }
            QLineEdit:focus{
                border: 1px solid rgb(102, 0, 0);
                background-color:rgb(219, 134, 134);
            }
        """
    
    def get_pushbutton_stylesheet():
        return """
            QPushButton {
                border: 0px;
                border-radius: 10px;
                color:rgb(240, 240, 217);
                background-color:#12646f;
                height: 25px;
                width: 150px;
                padding:10px;
            }
            
            QPushButton:hover {
                background-color: rgb(232, 232, 210);
                border: 1px solid  #12646f;
                color:  #12646f;
            }
            QPushButton:pressed {
                background-color: #12646f;
            }
        """

    def get_moodBtn_stylesheet(colour,colour_pressed):
        return f"""
            QPushButton {{
                padding: 0 10px;
                border: 0px;
                border-radius: 5px;
                color: rgb(240, 240, 217);
                background-color:{colour};
                height: 30px;
            }}
            QPushButton:hover {{
                background-color: rgb(232, 232, 210);
                border: 1px solid {colour};
                color: {colour};
            }}
            QPushButton:pressed {{
                background-color: {colour_pressed};
            }}
            """

    def get_moodBtn_stylesheet_invert(colour,colour_pressed):
        return f"""
            QPushButton {{
                padding: 0 10px;
                border: 0px;
                border-radius: 5px;
                color: {colour};
                background-color: none;
                height: 30px;
            }}
            QPushButton:hover {{
                background-color: {colour_pressed};
                border: 0px;
                color: {colour};
            }}
            QPushButton:pressed {{
                background-color: {colour_pressed};
            }}
            """
# rgb(152, 124, 200)
# rgb(171,142,229)

    def get_diary_textarea_stylesheet():
        return """
        QTextEdit{
            border: 0px;
            border-radius: 10px;
            background-color:rgb(227, 227, 206);
            padding: 10px;
        }
        QTextEdit:hover{
            background-color:rgb(211, 211, 191);
        }
        QTextEdit:focus{
            border: 1px solid rgb(31, 117, 253);
            background-color:rgb(211, 211, 191);
        }
        """

    def get_font(size):
        font = QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(size)
        return font

    