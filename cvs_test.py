import pandas as pd

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtGui
import webbrowser

Main_form_class = uic.loadUiType(r"C:\Users\hejin\miniproject\모두의 레시피 크롤링\list_UI.ui")[0]

class Menu_UI(QMainWindow,Main_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.list_w.itemDoubleClicked.connect(self.chkItemDoubleClicked)

        self.pushbtn.clicked.connect(self.gourl)

        fpath = r"C:\Users\hejin\miniproject\모두의 레시피 크롤링\소고기.csv"

        #특정 열 값을 리스트로 변경하기
        mr = pd.read_csv(fpath,names = ['A','B'],encoding='CP949')
        #이름
        name_cat = mr['A']
        #url
        url_cat = mr['B']

        #항목을 추가, 삽입하는 함수
        for i in range(40):
            self.list_w.insertItem(i,str(name_cat[i]))



    def chkItemDoubleClicked(self):
        #url로 이동

        list_item_num = self.list_w.currentRow() + 1
        self.qPixmap = QPixmap()
        self.qPixmap.load("C://Users//hejin//miniproject//모두의 레시피 크롤링//image//소고기//" + str(list_item_num) +".jpg")
        self.img_label.setPixmap(self.qPixmap)



    def gourl(self):
        #url 로 이동
        #파일 불러오기
        fpath = r"C:\Users\hejin\miniproject\모두의 레시피 크롤링\소고기.csv"
        mr = pd.read_csv(fpath,names = ['A','B'],encoding='CP949')
        list_item_num = self.list_w.currentRow()
        url_cat = mr['B']
        selected_url = str(url_cat[list_item_num])

        webbrowser.open(selected_url)

        list_item = self.list_w.selectedItems()

        for item in list_item:
            print(item.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Menu_UI()
    myWindow.show()
    app.exec_()