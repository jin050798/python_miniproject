import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from search import Search_UI

Main_form_class = uic.loadUiType(r"C:\Users\hejin\miniproject\모두의 레시피 크롤링\UI.ui")[0]

class WindowClass(QMainWindow, Main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.search_btn.clicked.connect(self.SearchbtnFunction)
        self.exit_btn.clicked.connect(self.ExitbtnFunction)

    def SearchbtnFunction(self):
        self.w = Search_UI()
        self.w.show()


    def ExitbtnFunction(self):

        btn = QPushButton('Quit', self)
        #첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고, 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력
        btn.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    myWindow = WindowClass()

    myWindow.show()

    app.exec_()