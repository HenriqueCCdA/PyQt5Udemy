import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Widget')
        self.setGeometry(50, 50, 600, 600)
        self.UI()

    def UI(self):
        #######################Main Menu#################################
        menubar = self.menuBar()
        file = menubar.addMenu('File')
        edit = menubar.addMenu('Edit')
        code = menubar.addMenu('Code')
        help_ = menubar.addMenu('help')

        #######################Sub Menu Items############################
        new = QAction('New', self)
        new.setShortcut('Ctrl+O')
        file.addAction(new)
        open = QAction('Open', self)
        file.addAction(open)
        exit = QAction('Exit', self)
        exit.setIcon(QIcon('icons/exit.png'))
        exit.triggered.connect(self.exitFunc)
        file.addAction(exit)

        self.show()


    def exitFunc(self):
        mbox = QMessageBox.information(self,
                                       'Warning',
                                       'Are you sore to exit?',
                                       QMessageBox.Yes|QMessageBox.No,
                                       QMessageBox.No)

        if mbox == QMessageBox.Yes:
            sys.exit()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
