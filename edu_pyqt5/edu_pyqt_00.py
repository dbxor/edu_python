import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QToolTip, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

__author__ = "kimyt@hanssem.com"

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Main Window'
        self.left = 300
        self.top = 300
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        path = os.getcwd()
    
        exitAction = QAction(QIcon(path+'/imgs/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        #QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        self.setToolTip('This is a <b>Push Button</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        

        #상태바
        self.statusBar().showMessage('Ready')
        
        #메뉴바
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)


        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(path+'/imgs/web.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.aboutToQuit.connect(app.deleteLater)
    ex = App()
    sys.exit(app.exec_())