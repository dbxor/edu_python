#%%
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("edu_pyqt_02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
   
        #기능을 연결하는 코드
        #self.button_Add.clicked.connect(self.fn_button_Add)

        self.groupRadio_Apple.clicked.connect(self.fn_group_radio_Select)
        self.groupRadio_Mac.clicked.connect(self.fn_group_radio_Select)

        self.checkBox_IOS.stateChanged.connect(self.fn_checkbox_Change)
        self.checkBox_AOS.stateChanged.connect(self.fn_checkbox_Change)

        self.lineEdit_Test.textChanged.connect(self.fn_lineEditText)
        self.lineEdit_Test.returnPressed.connect(self.fn_printText)
        self.button_ChangeText.clicked.connect(self.fn_changeText)

        #UI 초기값
        self.initUI()

    def initUI(self):
        path = os.getcwd()

        #메뉴 Action
        exitAction = QAction(QIcon(path+'/imgs/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)    

        #Status bar
        self.statusBar().showMessage('Ready')

        #Tool bar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        #Menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 600, 400)
        #self.show()

    #기능    
    def fn_button_Add(self):
        print("Button Add Clicked")

    def fn_group_radio_Select(self):
        if self.groupRadio_Apple.isChecked() : print("Radio Apple Checked")
        elif self.groupRadio_Mac.isChecked() : print("Radio Mac Checked")
        else :
            pass

    def fn_checkbox_Change(self):
        if self.checkBox_IOS.isChecked() : print("CheckBox IOS Checked")
        if self.checkBox_AOS.isChecked() : print("CheckBox AOS Checked")

    def fn_lineEditText(self):
        self.label_Test.setText(self.lineEdit_Test.text())

    def fn_printText(self):
        print(self.lineEdit_Test.text())

    def fn_changeText(self):
        self.lineEdit_Test.setText("Change Text")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
 
# %%
