import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hello world')
        self.create_widget()

    def get_click_button(self, n):
        def click():
            self.stroka.setText(self.stroka.text() + str(n))

        return click

    def create_widget(self):
        self.layout = QGridLayout()
        self.stroka = QLineEdit()
        self.layout.addWidget(self.stroka)
        self.buttons = []
        for i in range(9, -1, -1):
            self.buttons.append(QPushButton(str(i)))
            self.buttons[-1].clicked.connect(self.get_click_button(i))
            self.layout.addWidget(self.buttons[-1])
        self.setLayout(self.layout)

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
