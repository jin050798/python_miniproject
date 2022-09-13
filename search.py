import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import uic
#import crawling_menu

#웹 크롤링을 위한 라이브러리
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import os
import sys
import urllib.request
from time import sleep
import pyautogui
import pyperclip
import csv

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtGui
import webbrowser


import openpyxl


form_class = uic.loadUiType(r"C:\Users\hejin\miniproject\모두의 레시피 크롤링\Search_UI.ui")[0]

class Search_UI(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.radio_first.clicked.connect(self.groupboxRadFunction)
        self.radio_second.clicked.connect(self.groupboxRadFunction)
        self.radio_third.clicked.connect(self.groupboxRadFunction)


        self.Searchline.returnPressed.connect(self.printTextFunction)
        self.search_btn.clicked.connect(self.printTextFunction)


    def groupboxRadFunction(self):
        if self.radio_first.isChecked():
            return 1
        elif self.radio_second.isChecked():
            return 2
        elif self.radio_third.isChecked():
            return 3


    def printTextFunction(self):
        #b 에 검색어 저장
        global b
        b = self.Searchline.text()
        #a 에 라디오버튼 저장
        a = self.groupboxRadFunction()

        #브라우저 꺼짐 방지
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        #불필요한 에러 메시지 없애기
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        #chrome_options.add_argument('headless')

        service = Service(executable_path=ChromeDriverManager().install())
        #ChromDriverManager를 통해서 크롬드라이버를 설치하고 Service객체에 넣기
        driver = webdriver.Chrome(service=service, options=chrome_options)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')

        #웹페이지 해당주소 이동
        driver.implicitly_wait(5)#웹페이지가 로딩 될때까지 5초는 기다림
        driver.maximize_window()#화면 최대화
        driver.get('https://www.10000recipe.com/')

        #검색 부분 클릭
        search = driver.find_element(By.CSS_SELECTOR,"#srhRecipeText")
        search.click()

        if a == 1 :
            c = '초기 이유식'
            search.send_keys(c+b)
            search.send_keys(Keys.ENTER)
        elif a == 2:
            c = '중기 이유식'
            search.send_keys(c+b)
            search.send_keys(Keys.ENTER)
        elif a == 3:
            c = '후기 이유식'
            search.send_keys(c+b)
            search.send_keys(Keys.ENTER)

        correct = driver.find_element(By.CSS_SELECTOR,"#contents_area_full > ul > div > ul > li:nth-child(1)")
        correct.click()
        time.sleep(2)

        foods = driver.find_elements(By.CSS_SELECTOR,".common_sp_list_li")
        path = "C:\\Users\\hejin\\miniproject\\모두의 레시피 크롤링\\image\\"+b+"\\"

        try:
            if not os.path.exists(path):
                os.makedirs(path)
            else:
                print('같은 폴더가 존재합니다.')
                sys.exit(0)
        except OSError:
            print('os error')
            sys.exit(0)

        f = open("C:\\Users\\hejin\\miniproject\\모두의 레시피 크롤링\\" + b +".csv",'w',encoding='CP949', newline='')
        csvWritter = csv.writer(f)

        count = 1
        j = 1
        for food in foods:
            name = food.find_element(By.CSS_SELECTOR,".common_sp_caption_tit.line2").text
            url = food.find_element(By.CSS_SELECTOR,f"#contents_area_full > ul > ul > li:nth-child({j}) > div.common_sp_thumb > a").get_attribute('href')
            print(name,url)
            j = j+1
            csvWritter.writerow([name,url])

        f.close()

        imgs = driver.find_elements(By.CSS_SELECTOR,".common_sp_thumb")
        i = 1
        for img in imgs :
            imgUrl = img.find_element(By.XPATH,f"//*[@id=\"contents_area_full\"]/ul/ul/li[{i}]/div[1]/a/img").get_attribute("src")
            urllib.request.urlretrieve(imgUrl, path + str(count) +".jpg")
            count= count+1
            i = i+1

        reply = QMessageBox.question(self, '확인', '결과 확인',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes :
            self.w = Menu_UI()
            self.w.show()
            print("")
        elif reply == QMessageBox.No :
            print("")

form_windows = uic.loadUiType(r"C:\Users\hejin\miniproject\모두의 레시피 크롤링\list_UI.ui")[0]

class Menu_UI(QMainWindow,form_windows):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.list_w.itemDoubleClicked.connect(self.chkItemDoubleClicked)

        self.pushbtn.clicked.connect(self.gourl)

        fpath = "C://Users//hejin//miniproject//모두의 레시피 크롤링//"+b+".csv"

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
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("C://Users//hejin//miniproject//모두의 레시피 크롤링//image//"+b+"//" + str(list_item_num) +".jpg")
        self.img_label.setPixmap(self.qPixmapFileVar)



    def gourl(self):
        #url 로 이동
        #파일 불러오기
        fpath = "C://Users//hejin//miniproject//모두의 레시피 크롤링//"+b+".csv"
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
    myWindow = Search_UI()
    myWindow.show()
    app.exec_()