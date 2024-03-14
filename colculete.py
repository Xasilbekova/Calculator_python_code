from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5 import QtCore
from PyQt5 import QtGui
class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.collection = ""
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon("+"))
        
        self.display = QLineEdit("0")
        self.display.setStyleSheet("""
                                background-color: black; 
                                color: white;
                                padding: 70px;
                                font-size: 70px;
                                """)
        
        self.display.setAlignment(QtCore.Qt.AlignRight)

        self.btn1_1 = QPushButton("AC")
        self.btn1_1.setStyleSheet("""
                                background-color: gray;
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn1_3 = QPushButton("%")
        self.btn1_3.setStyleSheet("""
                                background-color: gray;
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn1_4 = QPushButton("/")
        self.btn1_4.setStyleSheet("""
                                background-color: orange;
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)

        self.btn2_1 = QPushButton("7")
        self.btn2_1.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn2_2 = QPushButton("8")
        self.btn2_2.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn2_3 = QPushButton("9")
        self.btn2_3.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn2_4 = QPushButton("*")
        self.btn2_4.setStyleSheet("""
                                background-color: orange;
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)

        self.btn3_1 = QPushButton("4")
        self.btn3_1.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn3_2 = QPushButton("5")
        self.btn3_2.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn3_3 = QPushButton("6")
        self.btn3_3.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn3_4 = QPushButton("-")
        self.btn3_4.setStyleSheet("""
                                background-color: orange;
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)

        self.btn4_1 = QPushButton("1")
        self.btn4_1.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn4_2 = QPushButton("2")
        self.btn4_2.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn4_3 = QPushButton("3")
        self.btn4_3.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn4_4 = QPushButton("+")
        self.btn4_4.setStyleSheet("""
                                background-color: orange;
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)

        self.btn5_1 = QPushButton("0")
        self.btn5_1.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        self.btn5_2 = QPushButton(".")
        self.btn5_2.setStyleSheet("""
                                background-color: rgb(45, 45, 45);
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                border: 1px solid; 
                                """)
        self.btn5_3 = QPushButton("=")
        self.btn5_3.setStyleSheet("""
                                background-color: orange;
                                color: white;
                                font-size: 40px;
                                padding: 20px;
                                border-radius: 40px;
                                """)
        

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        self.vbox = QVBoxLayout()

        self.hbox1.addWidget(self.btn1_1)
        self.hbox1.addWidget(self.btn1_3)
        self.hbox1.addWidget(self.btn1_4)

        self.hbox2.addWidget(self.btn2_1)
        self.hbox2.addWidget(self.btn2_2)
        self.hbox2.addWidget(self.btn2_3)
        self.hbox2.addWidget(self.btn2_4)

        self.hbox3.addWidget(self.btn3_1)
        self.hbox3.addWidget(self.btn3_2)
        self.hbox3.addWidget(self.btn3_3)
        self.hbox3.addWidget(self.btn3_4)

        self.hbox4.addWidget(self.btn4_1)
        self.hbox4.addWidget(self.btn4_2)
        self.hbox4.addWidget(self.btn4_3)
        self.hbox4.addWidget(self.btn4_4)

        self.hbox5.addWidget(self.btn5_1)
        self.hbox5.addWidget(self.btn5_2)
        self.hbox5.addWidget(self.btn5_3)

        self.vbox.addWidget(self.display)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)
        self.show()

        self.btn1_1.clicked.connect(self.remove)
        self.btn1_3.clicked.connect(self.on_click)
        self.btn1_4.clicked.connect(self.on_click)

        self.btn2_1.clicked.connect(self.on_click)
        self.btn2_2.clicked.connect(self.on_click)
        self.btn2_3.clicked.connect(self.on_click)
        self.btn2_4.clicked.connect(self.on_click)

        self.btn3_1.clicked.connect(self.on_click)
        self.btn3_2.clicked.connect(self.on_click)
        self.btn3_3.clicked.connect(self.on_click)
        self.btn3_4.clicked.connect(self.on_click)

        self.btn4_1.clicked.connect(self.on_click)
        self.btn4_2.clicked.connect(self.on_click)
        self.btn4_3.clicked.connect(self.on_click)
        self.btn4_4.clicked.connect(self.on_click)

        self.btn5_1.clicked.connect(self.on_click)
        self.btn5_2.clicked.connect(self.on_click)
        self.btn5_3.clicked.connect(self.resault)

        
    
    def on_click(self):
        text = self.sender().text()
        self.collection += text
        self.display.setText(self.collection)

    def resault(self):
        try:
            result = eval(self.collection)
            self.display.setText(str(result))
            self.collection = str(result)
        except Exception as e:
            self.display.setText("Error")
            self.collection = ""

    def remove(self):
        self.display.clear()
        self.collection = ""
        self.display.setText("0")

app = QApplication([])
win = Win()
win.setStyleSheet("background-color: black")
app.exec_()