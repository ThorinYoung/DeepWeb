class Theme:
    class Theme1:
        def __init__(self):
            # BUTTON COLOR
            self.extra_color = """background:rgb(0,143,150);"""
            # FRAME BACKGROUND
            self.background1 = """background:rgb(51,51,51);"""
            # PAGE BACKGROUND
            self.background2 = """background:rgb(91,90,90);"""
            self.word = """color:rgb(255,255,255);"""
            self.toodle = """QPushButton {
                border: none;
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
                background-color: rgb(0,178,178);
            }
            QPushButton:pressed {
                background-color: rgba(0,0,0,0);
            }"""
            self.label = """QLabel {
                color:rgb(255,255,255);
            }"""
            self.line_edit = """QLineEdit {
                color:rgb(255,255,255);
                border:2px solid rgb(51,51,51);
                border-radius:4px;
                background:rgb(51,51,51);
            }
            
            QLineEdit:disabled {
                color:rgb(255,255,255);
                border:2px solid rgb(112,112,112);
                border-radius:4px;
                background:rgb(112,112,112);
            }"""
            self.group_box = """QGroupBox{
                border:1px solid rgb(51,51,51);	
                border-radius:4px;
                color:white;
                background:rgb(91,90,90);
            }"""
            # Maximize, Minimize, Close
            self.button1 = """QPushButton {
                border: none;
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
                background-color: rgb(0,143,150);
            }
            QPushButton:pressed {	
                background-color: rgba(0,0,0,0);
            }"""
            # Button on left
            self.button2 = """QPushButton {
                border: none;
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
                background-color: rgb(91,90,90);
            }
            QPushButton:pressed {	
                background-color: rgba(0,0,0,0);
            }"""
            # Normal PushButton
            self.button3 = """QPushButton {
                border: 2px solid rgb(51,51,51);
                border-radius: 5px;	
                color:rgb(255,255,255);
                background-color: rgb(51,51,51);
            }
            QPushButton:hover {
                border: 2px solid rgb(0,143,150);
                background-color: rgb(0,143,150);
            }
            QPushButton:pressed {	
                border: 2px solid rgb(0,143,150);
                background-color: rgb(51,51,51);
            }
            
            QPushButton:disabled {	
                border-radius: 5px;	
                border: 2px solid rgb(112,112,112);
                background-color: rgb(112,112,112);
            }"""
            # Other PushButton
            self.button4 = """QPushButton {
                border: 2px solid rgb(51,51,51);
                border-radius: 5px;	
                color:rgb(255,255,255);
                background-color: rgb(51,51,51);
            }
            QPushButton:hover {
                border: 2px solid rgb(112,0,0);
                background-color: rgb(112,0,0);
            }
            QPushButton:pressed {	
                border: 2px solid rgb(112,0,0);
                background-color: rgb(51,51,51);
            }
            
            QPushButton:disabled {	
                border-radius: 5px;	
                border: 2px solid rgb(112,112,112);
                background-color: rgb(112,112,112);
            }"""
            self.progress = """QProgressBar
            {
                color:rgb(255,255,255);
                background-color :rgb(51,51,51);
                border : 2px;
                border-radius:4px;
            }
            
            QProgressBar::chunk{
                border : 2px;
                border-radius:4px;
                background-color:rgb(0,143,170);
            }"""
            self.combo_box = """QComboBox {
                border: 2px solid rgb(51,51,51);
                border-radius: 5px;	
                color:rgb(255,255,255);
                background-color: rgb(51,51,51);
            }
            
            QComboBox:hover {
                border: 2px solid rgb(0,143,170);
                border-radius: 5px;	
                color:rgb(255,255,255);
                background-color: rgb(0,143,170);
            }
            
            QComboBox:!editable, QComboBox::drop-down:editable {
                background: rgb(51,51,51);
            }
            
            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                    background:rgb(51,51,51);
            }
            
            QComboBox:on { /* shift the text when the popup opens */
                    padding-top: 3px;
                    padding-left: 4px;
            }
            
            QComboBox::drop-down {
                    subcontrol-origin: padding;
                    subcontrol-position: top right;
                    width: 15px;
            
                    border-left-width: 1px;
                    border-left-color: darkgray;
                    border-left-style: solid; /* just a single line */
                    border-top-right-radius: 5px; /* same radius as the QComboBox */
                    border-bottom-right-radius: 5px;
            }
            
            QComboBox::down-arrow {
                    image: url(icons/1x/bulletAsset 54.png);
            }
            
            QComboBox::down-arrow:on { /* shift the arrow when popup is open */
                    top: 1px;
                    left: 1px;
            }
            
            QComboBox::drop-down {
                    background:rgb(51,51,51);
            }
            
            QListView::item{
                    color: rgb(255,255,255);
            }
            QListView::item:selected{
                    background: rgb(0,143,150);
                    color: rgb(255,255,255);
            }
            QListView::item:hover{
                    background: rgb(0,143,150);
            }
            """
            self.radio_button = """QRadioButton {
                background:rgb(91,90,90);
                    color:white;
            }
            QRadioButton::indicator {
                    width:10px;
                    height:10px;
                    border-radius: 7px;
            }
            QRadioButton::indicator:checked {
                    background-color:rgb(0,143,170);
                    border: 2px solid rgb(51,51,51);
            }
            
            QRadioButton::indicator:unchecked {
                    background-color:rgb(91,90,90);
                    border:2px solid rgb(51,51,51);
            }"""
            self.check_box = """QCheckBox {
                    color:rgb(255,255,255);
            }
            
            QCheckBox::indicator {
                    width: 10px;
                    height: 10px;
            }
            
            QCheckBox::indicator:unchecked {
                    border:2px solid rgb(51,51,51);
                background:rgb(91,90,90);
            }
            
            QCheckBox::indicator:unchecked:pressed {
                border:2px solid rgb(51,51,51);
                background:rgb(0,143,170);
            }
            
            QCheckBox::indicator:checked {
                background-color:rgb(0,143,170);
                    border: 2px solid rgb(51,51,51);
            }
            
            QCheckBox::indicator:checked:pressed {
                    border:2px solid rgb(51,51,51);
                background:rgb(91,90,90);
            }"""
            self.horizontal_slider = """QSlider::groove:horizontal {
                    height:5px;
                    background: rgb(51,51,51);
            }
            
            QSlider::handle:horizontal {
                    background:rgb(0,143,170);
                    width: 10px;
                margin:-8px 0
            }
            
            QSlider::add-page:horizondal {
                    background:rgb(51,51,51);
            }
            
            QSlider::sub-page:horizondal {
                    background:rgb(51,51,51);
            }"""
            self.vertical_slider = """QSlider::groove:vertical {
                    background: red;
                    width:5px
            }
            
            QSlider::handle:vertical {
                    height: 10px;
                    background:rgb(0,143,170);
                margin:0 -8px
            }
            
            QSlider::add-page:vertical {
                    background:rgb(51,51,51);
            }
            
            QSlider::sub-page:vertical {
                    background:rgb(51,51,51);
            }"""

    class Theme2:
        def __init__(self):
            # BUTTON COLOR
            self.extra_color = """background:rgb(255,130,130);"""
            # FRAME BACKGROUND
            self.background1 = """background:rgb(255,160,160);"""
            # PAGE BACKGROUND
            self.background2 = """background:rgb(255,226,226);"""
            self.word = """color:rgb(150,130,130);"""
            self.toodle = """QPushButton {
                border: none;
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
                background-color: rgb(255,180,180);
            }
            QPushButton:pressed {
                background-color: rgba(0,0,0,0);
            }"""
            self.label = """QLabel {
                color:rgb(150,130,130);
            }"""
            self.line_edit = """QLineEdit {
                color:rgb(150,130,130);
                border:2px solid rgb(255,160,160);
                border-radius:4px;
                background:rgb(255,160,160);
            }

            QLineEdit:disabled {
                color:rgb(150,130,130);
                border:2px solid rgb(255,226,226);
                border-radius:4px;
                background:rgb(255,226,226);
            }"""
            self.group_box = """QGroupBox{
            	border:1px solid rgb(255,160,160);	
            	border-radius:4px;
            	color:rgb(150,130,130);
            	background:rgb(255,226,226);
            }"""
            # Maximize, Minimize, Close
            self.button1 = """QPushButton {
            	border: none;
            	background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
            	background-color: rgb(255,130,130);
            }
            QPushButton:pressed {	
            	background-color: rgba(0,0,0,0);
            }"""
            # Button on left
            self.button2 = """QPushButton {
            	border: none;
            	background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
            	background-color: rgb(255,226,226);
            }
            QPushButton:pressed {	
            	background-color: rgba(0,0,0,0);
            }"""
            # Normal PushButton
            self.button3 = """QPushButton {
            	border: 2px solid rgb(255,160,160);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(255,160,160);
            }
            QPushButton:hover {
            	border: 2px solid rgb(255,130,130);
            	background-color: rgb(255,130,130);
            }
            QPushButton:pressed {	
            	border: 2px solid rgb(255,130,130);
            	background-color: rgb(255,160,160);
            }

            QPushButton:disabled {	
            	border-radius: 5px;	
            	border: 2px solid rgb(112,112,112);
            	background-color: rgb(112,112,112);
            }"""
            # Other PushButton
            self.button4 = """QPushButton {
            	border: 2px solid rgb(255,160,160);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(255,160,160);
            }
            QPushButton:hover {
            	border: 2px solid rgb(112,0,0);
            	background-color: rgb(112,0,0);
            }
            QPushButton:pressed {	
            	border: 2px solid rgb(112,0,0);
            	background-color: rgb(255,160,160);
            }

            QPushButton:disabled {	
            	border-radius: 5px;	
            	border: 2px solid rgb(112,112,112);
            	background-color: rgb(112,112,112);
            }"""
            self.progress = """QProgressBar
            {
            	color:rgb(255,255,255);
            	background-color :rgb(255,160,160);
            	border : 2px;
            	border-radius:4px;
            }

            QProgressBar::chunk{
            	border : 2px;
            	border-radius:4px;
            	background-color:rgb(255,130,130);
            }"""
            self.combo_box = """QComboBox {
            	border: 2px solid rgb(255,160,160);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(255,160,160);
            }

            QComboBox:hover {
            	border: 2px solid rgb(150,130,130);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(150,130,130);
            }

            QComboBox:!editable, QComboBox::drop-down:editable {
            	background: rgb(255,160,160);
            }

            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                	background:rgb(255,160,160);
            }

            QComboBox:on { /* shift the text when the popup opens */
                	padding-top: 3px;
                	padding-left: 4px;
            }

            QComboBox::drop-down {
                	subcontrol-origin: padding;
                	subcontrol-position: top right;
                	width: 15px;

                	border-left-width: 1px;
                	border-left-color: darkgray;
                	border-left-style: solid; /* just a single line */
                	border-top-right-radius: 5px; /* same radius as the QComboBox */
                	border-bottom-right-radius: 5px;
            }

            QComboBox::down-arrow {
                	image: url(icons/1x/bulletAsset 54.png);
            }

            QComboBox::down-arrow:on { /* shift the arrow when popup is open */
                	top: 1px;
                	left: 1px;
            }

            QComboBox::drop-down {
                	background:rgb(255,160,160);
            }
            
            QListView::item{
                    color: rgb(150,130,130);
            }
            QListView::item:selected{
                    background: rgb(255,130,130);
                    color: rgb(255,255,255);
            }
            QListView::item:hover{
                    background: rgb(255,160,160);
            }
            """
            self.radio_button = """QRadioButton {
            	background:rgb(255,226,226);
                color:rgb(150,130,130);
            }
            QRadioButton::indicator {
                	width:10px;
                	height:10px;
                	border-radius: 7px;
            }
            QRadioButton::indicator:checked {
                	background-color:rgb(255,130,130);
                	border: 2px solid rgb(255,160,160);
            }

            QRadioButton::indicator:unchecked {
                	background-color:rgb(255,226,226);
                	border:2px solid rgb(255,160,160);
            }"""
            self.check_box = """QCheckBox {
                	color:rgb(255,255,255);
            }

            QCheckBox::indicator {
                	width: 10px;
                	height: 10px;
            }

            QCheckBox::indicator:unchecked {
                	border:2px solid rgb(255,160,160);
            	background:rgb(255,226,226);
            }

            QCheckBox::indicator:unchecked:pressed {
            	border:2px solid rgb(255,160,160);
               	background:rgb(150,130,130);
            }

            QCheckBox::indicator:checked {
            	background-color:rgb(150,130,130);
                	border: 2px solid rgb(255,160,160);
            }

            QCheckBox::indicator:checked:pressed {
                	border:2px solid rgb(255,160,160);
            	background:rgb(255,226,226);
            }"""
            self.horizontal_slider = """QSlider::groove:horizontal {
                	height:5px;
                	background: rgb(255,160,160);
            }

            QSlider::handle:horizontal {
                	background:rgb(255,130,130);
                	width: 10px;
            	margin:-8px 0
            }

            QSlider::add-page:horizondal {
                	background:rgb(255,160,160);
            }

            QSlider::sub-page:horizondal {
                	background:rgb(255,160,160);
            }"""
            self.vertical_slider = """QSlider::groove:vertical {
                	background: red;
                	width:5px
            }

            QSlider::handle:vertical {
                	height: 10px;
                	background:rgb(255,130,130);
            	margin:0 -8px
            }

            QSlider::add-page:vertical {
                	background:rgb(255,160,160);
            }

            QSlider::sub-page:vertical {
                	background:rgb(255,160,160);
            }"""

    class Theme3:
        def __init__(self):
            # BUTTON(TOODLE) COLOR
            self.extra_color = """background:rgb(255,215,0);"""
            # FRAME BACKGROUND
            self.background1 = """background:rgb(1,77,103);"""
            # PAGE BACKGROUND
            self.background2 = """background:rgb(96,143,159);"""
            self.word = """color:rgb(255,255,10);"""
            self.toodle = """QPushButton {
                border: none;
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
                background-color: rgb(251,178,23);
            }
            QPushButton:pressed {
                background-color: rgba(0,0,0,0);
            }"""
            self.label = """QLabel {
                color:rgb(255,255,10);
            }"""
            self.line_edit = """QLineEdit {
                color:rgb(255,255,10);
                border:2px solid rgb(1,77,103);
                border-radius:4px;
                background:rgb(1,77,103);
            }

            QLineEdit:disabled {
                color:rgb(255,255,10);
                border:2px solid rgb(96,143,159);
                border-radius:4px;
                background:rgb(96,143,159);
            }"""
            self.group_box = """QGroupBox{
            	border:1px solid rgb(1,77,103);	
            	border-radius:4px;
            	color:rgb(255,255,10);
            	background:rgb(96,143,159);
            }"""
            # Maximize, Minimize, Close
            self.button1 = """QPushButton {
            	border: none;
            	background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
            	background-color: rgb(255,215,0);
            }
            QPushButton:pressed {	
            	background-color: rgba(0,0,0,0);
            }"""
            # Button on left
            self.button2 = """QPushButton {
            	border: none;
            	background-color: rgba(0,0,0,0);
            }
            QPushButton:hover {
            	background-color: rgb(96,143,159);
            }
            QPushButton:pressed {	
            	background-color: rgba(0,0,0,0);
            }"""
            # Normal PushButton
            self.button3 = """QPushButton {
            	border: 2px solid rgb(1,77,103);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(1,77,103);
            }
            QPushButton:hover {
            	border: 2px solid rgb(255,215,0);
            	background-color: rgb(255,215,0);
            }
            QPushButton:pressed {	
            	border: 2px solid rgb(255,215,0);
            	background-color: rgb(1,77,103);
            }

            QPushButton:disabled {	
            	border-radius: 5px;	
            	border: 2px solid rgb(112,112,112);
            	background-color: rgb(112,112,112);
            }"""
            # Other PushButton
            self.button4 = """QPushButton {
            	border: 2px solid rgb(1,77,103);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(1,77,103);
            }
            QPushButton:hover {
            	border: 2px solid rgb(112,0,0);
            	background-color: rgb(112,0,0);
            }
            QPushButton:pressed {	
            	border: 2px solid rgb(112,0,0);
            	background-color: rgb(1,77,103);
            }

            QPushButton:disabled {	
            	border-radius: 5px;	
            	border: 2px solid rgb(112,112,112);
            	background-color: rgb(112,112,112);
            }"""
            self.progress = """QProgressBar
            {
            	color:rgb(255,255,255);
            	background-color :rgb(1,77,103);
            	border : 2px;
            	border-radius:4px;
            }

            QProgressBar::chunk{
            	border : 2px;
            	border-radius:4px;
            	background-color:rgb(255,215,0);
            }"""
            self.combo_box = """QComboBox {
            	border: 2px solid rgb(1,77,103);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(1,77,103);
            }

            QComboBox:hover {
            	border: 2px solid rgb(255,255,10);
            	border-radius: 5px;	
            	color:rgb(255,255,255);
            	background-color: rgb(255,255,10);
            }

            QComboBox:!editable, QComboBox::drop-down:editable {
            	background: rgb(1,77,103);
            }

            QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                	background:rgb(1,77,103);
            }

            QComboBox:on { /* shift the text when the popup opens */
                	padding-top: 3px;
                	padding-left: 4px;
            }

            QComboBox::drop-down {
                	subcontrol-origin: padding;
                	subcontrol-position: top right;
                	width: 15px;

                	border-left-width: 1px;
                	border-left-color: darkgray;
                	border-left-style: solid; /* just a single line */
                	border-top-right-radius: 5px; /* same radius as the QComboBox */
                	border-bottom-right-radius: 5px;
            }

            QComboBox::down-arrow {
                	image: url(icons/1x/bulletAsset 54.png);
            }

            QComboBox::down-arrow:on { /* shift the arrow when popup is open */
                	top: 1px;
                	left: 1px;
            }

            QComboBox::drop-down {
                	background:rgb(1,77,103);
            }

            QListView::item{
                    color: rgb(255,255,10);
            }
            QListView::item:selected{
                    background: rgb(255,215,0);
                    color: rgb(255,255,255);
            }
            QListView::item:hover{
                    background: rgb(1,77,103);
            }
            """
            self.radio_button = """QRadioButton {
            	background:rgb(96,143,159);
                color:rgb(255,255,10);
            }
            QRadioButton::indicator {
                	width:10px;
                	height:10px;
                	border-radius: 7px;
            }
            QRadioButton::indicator:checked {
                	background-color:rgb(255,215,0);
                	border: 2px solid rgb(1,77,103);
            }

            QRadioButton::indicator:unchecked {
                	background-color:rgb(96,143,159);
                	border:2px solid rgb(1,77,103);
            }"""
            self.check_box = """QCheckBox {
                	color:rgb(255,255,255);
            }

            QCheckBox::indicator {
                	width: 10px;
                	height: 10px;
            }

            QCheckBox::indicator:unchecked {
                	border:2px solid rgb(1,77,103);
            	background:rgb(96,143,159);
            }

            QCheckBox::indicator:unchecked:pressed {
            	border:2px solid rgb(1,77,103);
               	background:rgb(255,255,10);
            }

            QCheckBox::indicator:checked {
            	background-color:rgb(255,255,10);
                	border: 2px solid rgb(1,77,103);
            }

            QCheckBox::indicator:checked:pressed {
                	border:2px solid rgb(1,77,103);
            	background:rgb(96,143,159);
            }"""
            self.horizontal_slider = """QSlider::groove:horizontal {
                	height:5px;
                	background: rgb(1,77,103);
            }

            QSlider::handle:horizontal {
                	background:rgb(255,215,0);
                	width: 10px;
            	margin:-8px 0
            }

            QSlider::add-page:horizondal {
                	background:rgb(1,77,103);
            }

            QSlider::sub-page:horizondal {
                	background:rgb(1,77,103);
            }"""
            self.vertical_slider = """QSlider::groove:vertical {
                	background: red;
                	width:5px
            }

            QSlider::handle:vertical {
                	height: 10px;
                	background:rgb(255,215,0);
            	margin:0 -8px
            }

            QSlider::add-page:vertical {
                	background:rgb(1,77,103);
            }

            QSlider::sub-page:vertical {
                	background:rgb(1,77,103);
            }"""

    class Theme4:
        def __init__(self):
            # BUTTON COLOR
            self.extra_color = """background:rgb(3,35,14);"""
            # FRAME BACKGROUND
            self.background1 = """background:rgb(64,116,52);"""
            # PAGE BACKGROUND
            self.background2 = """background:rgb(101,147,74);"""
            self.word = """color:rgb(160,191,124);"""
            self.toodle = """QPushButton {
                            border: none;
                            background-color: rgba(0,0,0,0);
                        }
                        QPushButton:hover {
                            background-color: rgb(30,70,30);
                        }
                        QPushButton:pressed {
                            background-color: rgba(0,0,0,0);
                        }"""
            self.label = """QLabel {
                            color:rgb(200,240,200);
                        }"""
            self.line_edit = """QLineEdit {
                            color:rgb(160,191,124);
                            border:2px solid rgb(64,116,52);
                            border-radius:4px;
                            background:rgb(64,116,52);
                        }

                        QLineEdit:disabled {
                            color:rgb(160,191,124);
                            border:2px solid rgb(101,147,74);
                            border-radius:4px;
                            background:rgb(101,147,74);
                        }"""
            self.group_box = """QGroupBox{
                        	border:1px solid rgb(64,116,52);	
                        	border-radius:4px;
                        	color:rgb(200,240,200);
                        	background:rgb(101,147,74);
                        }"""
            # Maximize, Minimize, Close
            self.button1 = """QPushButton {
                        	border: none;
                        	background-color: rgba(0,0,0,0);
                        }
                        QPushButton:hover {
                        	background-color: rgb(50,100,50);
                        }
                        QPushButton:pressed {	
                        	background-color: rgba(0,0,0,0);
                        }"""
            # Button on left
            self.button2 = """QPushButton {
                        	border: none;
                        	background-color: rgba(0,0,0,0);
                        }
                        QPushButton:hover {
                        	background-color: rgb(101,147,74);
                        }
                        QPushButton:pressed {	
                        	background-color: rgba(0,0,0,0);
                        }"""
            # Normal PushButton
            self.button3 = """QPushButton {
                        	border: 2px solid rgb(64,116,52);
                        	border-radius: 5px;	
                        	color:rgb(255,255,255);
                        	background-color: rgb(64,116,52);
                        }
                        QPushButton:hover {
                        	border: 2px solid rgb(50,100,50);
                        	background-color: rgb(50,100,50);
                        }
                        QPushButton:pressed {	
                        	border: 2px solid rgb(50,100,50);
                        	background-color: rgb(64,116,52);
                        }

                        QPushButton:disabled {	
                        	border-radius: 5px;	
                        	border: 2px solid rgb(112,112,112);
                        	background-color: rgb(112,112,112);
                        }"""
            # Other PushButton
            self.button4 = """QPushButton {
                        	border: 2px solid rgb(64,116,52);
                        	border-radius: 5px;	
                        	color:rgb(255,255,255);
                        	background-color: rgb(64,116,52);
                        }
                        QPushButton:hover {
                        	border: 2px solid rgb(112,0,0);
                        	background-color: rgb(112,0,0);
                        }
                        QPushButton:pressed {	
                        	border: 2px solid rgb(112,0,0);
                        	background-color: rgb(64,116,52);
                        }

                        QPushButton:disabled {	
                        	border-radius: 5px;	
                        	border: 2px solid rgb(112,112,112);
                        	background-color: rgb(112,112,112);
                        }"""
            self.progress = """QProgressBar
                        {
                        	color:rgb(255,255,255);
                        	background-color :rgb(64,116,52);
                        	border : 2px;
                        	border-radius:4px;
                        }

                        QProgressBar::chunk{
                        	border : 2px;
                        	border-radius:4px;
                        	background-color:rgb(50,100,50);
                        }"""
            self.combo_box = """QComboBox {
                        	border: 2px solid rgb(64,116,52);
                        	border-radius: 5px;	
                        	color:rgb(255,255,255);
                        	background-color: rgb(64,116,52);
                        }

                        QComboBox:hover {
                        	border: 2px solid rgb(160,191,124);
                        	border-radius: 5px;	
                        	color:rgb(255,255,255);
                        	background-color: rgb(160,191,124);
                        }

                        QComboBox:!editable, QComboBox::drop-down:editable {
                        	background: rgb(64,116,52);
                        }

                        QComboBox:!editable:on, QComboBox::drop-down:editable:on {
                            	background:rgb(64,116,52);
                        }

                        QComboBox:on { /* shift the text when the popup opens */
                            	padding-top: 3px;
                            	padding-left: 4px;
                        }

                        QComboBox::drop-down {
                            	subcontrol-origin: padding;
                            	subcontrol-position: top right;
                            	width: 15px;

                            	border-left-width: 1px;
                            	border-left-color: darkgray;
                            	border-left-style: solid; /* just a single line */
                            	border-top-right-radius: 5px; /* same radius as the QComboBox */
                            	border-bottom-right-radius: 5px;
                        }

                        QComboBox::down-arrow {
                            	image: url(icons/1x/bulletAsset 54.png);
                        }

                        QComboBox::down-arrow:on { /* shift the arrow when popup is open */
                            	top: 1px;
                            	left: 1px;
                        }

                        QComboBox::drop-down {
                            	background:rgb(64,116,52);
                        }

                        QListView::item{
                                color: rgb(200,240,200);
                        }
                        QListView::item:selected{
                                background: rgb(50,100,50);
                                color: rgb(255,255,255);
                        }
                        QListView::item:hover{
                                background: rgb(64,116,52);
                        }
                        """
            self.radio_button = """QRadioButton {
                        	background:rgb(101,147,74);
                            color:rgb(200,240,200);
                        }
                        QRadioButton::indicator {
                            	width:10px;
                            	height:10px;
                            	border-radius: 7px;
                        }
                        QRadioButton::indicator:checked {
                            	background-color:rgb(50,100,50);
                            	border: 2px solid rgb(64,116,52);
                        }

                        QRadioButton::indicator:unchecked {
                            	background-color:rgb(101,147,74);
                            	border:2px solid rgb(64,116,52);
                        }"""
            self.check_box = """QCheckBox {
                            	color:rgb(255,255,255);
                        }

                        QCheckBox::indicator {
                            	width: 10px;
                            	height: 10px;
                        }

                        QCheckBox::indicator:unchecked {
                            	border:2px solid rgb(64,116,52);
                        	background:rgb(101,147,74);
                        }

                        QCheckBox::indicator:unchecked:pressed {
                        	border:2px solid rgb(64,116,52);
                           	background:rgb(160,191,124);
                        }

                        QCheckBox::indicator:checked {
                        	background-color:rgb(160,191,124);
                            	border: 2px solid rgb(64,116,52);
                        }

                        QCheckBox::indicator:checked:pressed {
                            	border:2px solid rgb(64,116,52);
                        	background:rgb(101,147,74);
                        }"""
            self.horizontal_slider = """QSlider::groove:horizontal {
                            	height:5px;
                            	background: rgb(64,116,52);
                        }

                        QSlider::handle:horizontal {
                            	background:rgb(50,100,50);
                            	width: 10px;
                        	margin:-8px 0
                        }

                        QSlider::add-page:horizondal {
                            	background:rgb(64,116,52);
                        }

                        QSlider::sub-page:horizondal {
                            	background:rgb(64,116,52);
                        }"""
            self.vertical_slider = """QSlider::groove:vertical {
                            	background: red;
                            	width:5px
                        }

                        QSlider::handle:vertical {
                            	height: 10px;
                            	background:rgb(50,100,50);
                        	margin:0 -8px
                        }

                        QSlider::add-page:vertical {
                            	background:rgb(64,116,52);
                        }

                        QSlider::sub-page:vertical {
                            	background:rgb(64,116,52);
                        }"""
