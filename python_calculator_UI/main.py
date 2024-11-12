from PyQt6 import uic 
import sys 
from PyQt6.QtWidgets import QPushButton, QLabel, QDialog, QApplication

calc = ""


class mainWindow(QDialog):
    global calc

    def __init__(self):

        super().__init__()
        uic.loadUi("dialog.ui", self)
        self.setWindowTitle("Calculator")

        # --------------------------------------------------------

        self.button_0 = self.findChild(QPushButton, "button_0")
        self.button_1 = self.findChild(QPushButton, "button_1")
        self.button_2 = self.findChild(QPushButton, "button_2")
        self.button_3 = self.findChild(QPushButton, "button_3")
        self.button_4 = self.findChild(QPushButton, "button_4")
        self.button_5 = self.findChild(QPushButton, "button_5")
        self.button_6 = self.findChild(QPushButton, "button_6")
        self.button_7 = self.findChild(QPushButton, "button_7")
        self.button_8 = self.findChild(QPushButton, "button_8")
        self.button_9 = self.findChild(QPushButton, "button_9")

        self.button_add = self.findChild(QPushButton, "button_add")
        self.button_sub = self.findChild(QPushButton, "button_sub")
        self.button_mult = self.findChild(QPushButton, "button_mult")
        self.button_div = self.findChild(QPushButton, "button_div")
        self.button_enter = self.findChild(QPushButton, "button_enter")
        self.button_exp = self.findChild(QPushButton, "button_exp")

        self.display = self.findChild(QLabel, "display")

        # --------------------------------------------------------

        self.button_0.clicked.connect(lambda: self.add_to_calc(0))
        self.button_1.clicked.connect(lambda: self.add_to_calc(1))
        self.button_2.clicked.connect(lambda: self.add_to_calc(2))
        self.button_3.clicked.connect(lambda: self.add_to_calc(3))
        self.button_4.clicked.connect(lambda: self.add_to_calc(4))
        self.button_5.clicked.connect(lambda: self.add_to_calc(5))
        self.button_6.clicked.connect(lambda: self.add_to_calc(6))
        self.button_7.clicked.connect(lambda: self.add_to_calc(7))
        self.button_8.clicked.connect(lambda: self.add_to_calc(8))
        self.button_9.clicked.connect(lambda: self.add_to_calc(9))

        self.button_add.clicked.connect(lambda: self.add_to_calc("+"))
        self.button_sub.clicked.connect(lambda: self.add_to_calc("-"))
        self.button_mult.clicked.connect(lambda: self.add_to_calc("*"))
        self.button_div.clicked.connect(lambda: self.add_to_calc("/"))
        self.button_exp.clicked.connect(lambda: self.add_to_calc("**"))
        self.button_enter.clicked.connect(self.calculate)

        # --------------------------------------------------------

        
    def calculate(self):
        global calc
        result = eval(calc)
        calc = str(result)
        self.display.setText(str(result))


    def add_to_calc(self, value):
        global calc
        calc += str(value)
        self.display.setText(calc)


    
app = QApplication(sys.argv)
UI = mainWindow()
UI.show()
app.exec()

