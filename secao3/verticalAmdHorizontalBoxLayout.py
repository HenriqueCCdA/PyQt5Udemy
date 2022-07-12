import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vertical and Horizontal Box Layouts')
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottonLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottonLayout)

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()

        topLayout.setContentsMargins(100, 10, 20, 20) # left, top, rigth, botton

        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combo)
        bottonLayout.setContentsMargins(150, 10, 150, 10)
        bottonLayout.addWidget(btn1)
        bottonLayout.addWidget(btn2)

        self.setLayout(mainLayout)

        self.show()

def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
