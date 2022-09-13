import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QAction, qApp, QDesktopWidget, QLabel, QVBoxLayout, QHBoxLayout, QTabWidget
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('이유식 찾기')
        #창 제목 설정하기
        self.setWindowIcon(QIcon(r'C:\Users\hejin\miniproject\모두의 레시피 크롤링\food.png'))
        self.resize(500, 500)
        self.center()
        #창 위치와 크기 설정

        #나가기 버튼
        #btn = QPushButton('Quit', self)
        #첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고, 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력
        #btn.move(50, 50)
        #btn.resize(btn.sizeHint())
        #btn.clicked.connect(QCoreApplication.instance().quit)
        
        exitAction = QAction(QIcon(r'C:\Users\hejin\miniproject\모두의 레시피 크롤링\logout.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')


        widget = QWidget()
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        

        self.show()
        
    def center(self):
        #창의 위치와 크기정보 가지고옴
        qr = self.frameGeometry()
        #사용하는 모니터 화면의 가운데 위치를 파악
        cp = QDesktopWidget().availableGeometry().center()
        #창의 직사각형 위치를 화면의 중심의 위치로 이동
        qr.moveCenter(cp)
        #현재 창을 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킴
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #어플리케이션 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())