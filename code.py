import sys

from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(' ')
        self.create_widget()
        self.stroka.setReadOnly(True)

    def get_click_button(self, n):
        def click():
            self.stroka.setText(self.stroka.text() + str(n))

        return click

    def create_widget(self):
        self.layoutV = QVBoxLayout()
        self.layoutH123 = QHBoxLayout()
        self.layoutH456 = QHBoxLayout()
        self.layoutH789 = QHBoxLayout()
        self.layoutH0_plus_minus = QHBoxLayout()
        self.layoutHmul_div_equ = QHBoxLayout()
        self.delete_button = QPushButton("DELETE")

        self.stroka = QLineEdit()
        self.layoutV.addWidget(self.stroka)
        self.layoutV.addWidget(self.delete_button)
        self.layoutV.addLayout(self.layoutH123)
        self.layoutV.addLayout(self.layoutH456)
        self.layoutV.addLayout(self.layoutH789)
        self.layoutV.addLayout(self.layoutH0_plus_minus)
        self.layoutV.addLayout(self.layoutHmul_div_equ)
        self.buttons = []
        self.plus_button = QPushButton("+")
        self.minus_button = QPushButton("-")
        self.zero_button = QPushButton("0")
        self.multiplication_button = QPushButton("*")
        self.division_button = QPushButton("/")
        self.equals_button = QPushButton("=")

        for i in range(1, 4):
            self.buttons.append(QPushButton(str(i)))
            self.buttons[-1].clicked.connect(self.get_click_button(i))
            self.layoutH123.addWidget(self.buttons[-1])

        for i in range(4, 7):
            self.buttons.append(QPushButton(str(i)))
            self.buttons[-1].clicked.connect(self.get_click_button(i))
            self.layoutH456.addWidget(self.buttons[-1])

        for i in range(7, 10):
            self.buttons.append(QPushButton(str(i)))
            self.buttons[-1].clicked.connect(self.get_click_button(i))
            self.layoutH789.addWidget(self.buttons[-1])

        self.plus_button.clicked.connect(self.click_plus_button)
        self.minus_button.clicked.connect(self.click_minus_button)
        self.zero_button.clicked.connect(self.click_zero_button)
        self.multiplication_button.clicked.connect(self.click_multiplication_button)
        self.division_button.clicked.connect(self.click_division_button)
        self.equals_button.clicked.connect(self.click_equals_button)
        self.delete_button.clicked.connect(self.click_delete_button)
        self.h_zero_plus_minus = [self.zero_button, self.plus_button, self.minus_button]
        for t in range(1,4):
            self.layoutH0_plus_minus.addWidget(self.h_zero_plus_minus[int(t-1)])

        self.h_mul_div_equ = [self.multiplication_button, self.division_button, self.equals_button]
        for t in range(1, 4):
            self.layoutHmul_div_equ.addWidget(self.h_mul_div_equ[int(t - 1)])

        self.setLayout(self.layoutV)

    def click_delete_button(self):
        self.stroka.setText("")

    def click_plus_button(self):
        self.stroka.setText(self.stroka.text() + str("+"))

    def click_minus_button(self):
        self.stroka.setText(self.stroka.text() + str("-"))

    def click_zero_button(self):
        self.stroka.setText(self.stroka.text() + str("0"))

    def click_multiplication_button(self):
        self.stroka.setText(self.stroka.text() + str("*"))

    def click_division_button(self):
        self.stroka.setText(self.stroka.text() + str("/"))

    def click_equals_button(self):
        if "+" in self.stroka.text():
            a = self.stroka.text().split("+")
            self.stroka.setText(str(int(a[0])+int(a[1])))
        elif "-" in self.stroka.text():
            a = self.stroka.text().split("-")
            self.stroka.setText(str(int(a[0])-int(a[1])))
        elif "*" in self.stroka.text():
            a = self.stroka.text().split("*")
            self.stroka.setText(str(int(a[0])*int(a[1])))
        elif "/" in self.stroka.text():
            a = self.stroka.text().split("/")
            self.stroka.setText(str(int(a[0])/int(a[1])))


app = QApplication(sys.argv)
widget = MyWidget()
widget.setFixedSize(100,200)
widget.show()
sys.exit(app.exec_())
