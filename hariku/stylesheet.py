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

    def get_combobox_stylesheet():
        return """
        QComboBox {
            padding: 5px;
            border-radius: 5px;
            color:  black;
            background-color:rgb(40, 186, 130) ;
            height: 25px;
            width: 100px;
        }
        QComboBox:hover {
            background-color: rgb(232, 232, 210);
            border: 1px solid  rgb(40, 186, 130);;
        }
        QComboBox::drop-down{
            background-color:rgb(40, 186, 130) ;
            color:rgb(240, 240, 217);
            font-weight:bold;
            padding:0px;
            border-radius: 5px;
            width:25px;
        }
        QComboBox::down-arrow{
               image:url(img/combobox_down_arrow.png);
            width: 10px; 
            height: 10px;
        }
        QListView{
            border:none;
            color:rgb(87, 96, 134);
            background-color:rgb(255, 255, 255);
            font-weight: bold;
            selection-background-color:rgb(40, 186, 130);
            show-decoration-selected:1;
            margin-left:-10px;
            padding-left:15px;
        }
        QComboBox QAbstractItemView {
            outline: none;
        }
        """
        
    def get_scrollarea_stylesheet():
        return """
        QScrollArea{    
            border-radius: 0;
        }
        QScrollArea QWidget{   
            background-color:rgb(227, 227, 206);
            color:black;
        }
        /* VERTICAL SCROLLBAR */
        QScrollBar:vertical {
            border: none;
            background: rgb(205, 199, 190);
            width: 14px;
            margin: 15px 0 15px 0;
            border-radius: 0px;
        }
        /*  HANDLE BAR VERTICAL */
        QScrollBar::handle:vertical {    
            background-color: rgb(118, 97, 97);
            min-height: 30px;
            border-radius: 7px;
        }
        QScrollBar::handle:vertical:hover{    
            background-color: rgb(81, 196, 211);
        }
        QScrollBar::handle:vertical:pressed {    
            background-color: rgb(18, 110, 130);
        }
        /* BTN TOP - SCROLLBAR */
        QScrollBar::sub-line:vertical {
            border: none;
            background-color: rgb(205, 199, 190);
            height: 15px;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical:hover {    
            background-color: rgb(81, 196, 211);
        }
        QScrollBar::sub-line:vertical:pressed {    
            background-color: rgb(18, 110, 130);
        }
        /* BTN BOTTOM - SCROLLBAR */
        QScrollBar::add-line:vertical {
            border: none;
            background-color: rgb(205, 199, 190);
            height: 15px;
            border-bottom-left-radius: 7px;
            border-bottom-right-radius: 7px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::add-line:vertical:hover {    
            background-color:rgb(81, 196, 211);
        }
        QScrollBar::add-line:vertical:pressed {    
            background-color: rgb(18, 110, 130);
        }
        /* RESET ARROW */
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
            background: none;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        """
    
    def get_dateedit_stylesheet():
        return """
        QDateEdit {
            background-color: rgb(188, 212, 203);
            color: rgb(12, 61, 42); 
            border-radius:7px;
            width:190px;
            padding: 7px;
        }

        QDateEdit::up-button{
            margin:1px;
            margin-right: 2px;
            border-radius:3px;
            image:url(assets/combobox_up_arrow.png);
            background-color: rgba(0,0,0,40%);
        }

        QDateEdit::down-button{
            margin:1px;
            margin-right: 2px;
            border-radius:2px;
            image:url(assets/combobox_down_arrow.png);
            background-color: rgba(0,0,0,40%);
        }

        QDateEdit::down-button:hover, QDateEdit::up-button:hover{
            background-color: rgba(0,0,0,50%);
        }
        """