import sys

from PyQt5.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Employees')
        self.setGeometry(450, 150, 750, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        self.employeeList = QListWidget()
        self.btnNew = QPushButton('New')
        self.btnUpdate = QPushButton('Update')
        self.btnDelete = QPushButton('Delete')

    def layouts(self):
        #########################Layouts#############################
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()

        ################Adding child layouts to main layout###########
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 40)
        self.mainLayout.addLayout(self.rightMainLayout, 60)

        ##################adding widgets to layouts ##################
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)

        ################Setting main window layout####################
        self.setLayout(self.mainLayout)


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()
