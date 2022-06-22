import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 350, 350)
        self.UI()


    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Enter your name')
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText('Enter your name')
        self.name.move(150, 50)
        self.surname.move(150, 80)
        self.remember=QCheckBox("Remember me", self)
        self.remember.move(150, 110)
        button=QPushButton('Submmit', self)
        button.move(200, 140)
        button.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if self.remember.isChecked():
            print(f'Name: {self.name.text()} \nSurname: {self.surname.text()} \nRemember me checked')
        else:
            print(f'Name: {self.name.text()} \nSurname: {self.surname.text()} \nRemember me not checked')


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()