import email
from email.headerregistry import Address
import os
import sys
import sqlite3

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PIL import Image


con = sqlite3.connect('employees.db')
cur = con.cursor()
defaultImg = 'person.png'


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
        self.btnNew.clicked.connect(self.addEmployee)
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

    def addEmployee(self):
        self.newEmployee = AddEmployee()
        self.close()


class AddEmployee(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Employees')
        self.setGeometry(450, 150, 350, 600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layout()

    def mainDesign(self):
        #################Top Layout widgets#######################################
        self.setStyleSheet('Background-color:white;font-size:14pt;font-family:Times')
        self.title = QLabel('Add Person')
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap('icons/person.png'))
        #################Bottom Layout Widgets####################################
        self.nameLbl = QLabel('Name :')
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText('Enter Employee Name')

        self.surnameLbl = QLabel('Surname :')
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText('Enter Employee Surname')

        self.phoneLbl = QLabel('Phone :')
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText('Enter Employee Phone Number')

        self.emailLbl = QLabel('Email :')
        self.emailEntry = QLineEdit()
        self.emailEntry.setPlaceholderText('Enter Employee Email')

        self.imgLbl = QLabel('Pictute: ')
        self.imgButton = QPushButton('Browse')
        self.imgButton.setStyleSheet('background-color:orange;font-size:10pt')
        self.imgButton.clicked.connect(self.uploadImage)

        self.addressLbl = QLabel('Address :')
        self.addressEditor = QTextEdit()
        self.addButton = QPushButton('Add')
        self.addButton.setStyleSheet('background-color:orange;font-size:10pt')

        self.addButton.clicked.connect(self.addEmployee)

    def layout(self):
        #########################Creating main layouts############################
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        ###############adding child layouts to main layout########################
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        ###############adding widget to layouts###################################

        ############################top layout####################################
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110, 20, 10, 30) #left, top, rigth, bottom

        ############################bottom layou##################################
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl, self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgButton)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addRow('', self.addButton)

        ##############setting main layout window##################################
        self.setLayout(self.mainLayout)


    def uploadImage(self):
        global defaultImg
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')

        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save(f'images/{defaultImg}')

    def addEmployee(self):
        global defaultImg
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText()
        if name and surname and phone != "":
            try:
                query = 'INSERT INTO employees (name, surname, phone, email, img, address) VALUES (?,?,?,?,?,?)'
                cur.execute(query, (name, surname, phone, email, img, address))
                con.commit()
                QMessageBox.information(self, 'Success', 'Person has been added')
            except:
                QMessageBox.information(self, 'Warning', 'Person has not been added')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not been empty')


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()
