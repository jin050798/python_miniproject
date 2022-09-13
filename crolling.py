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

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument('headless')

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

a = int(input("숫자를 입력하세요 : (1,2,3)"))
b = input("주 재료를 입력하세요 : ")
#검색어 입력

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

#정확순 클릭
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
    
count = 1
j = 1
for food in foods:
    name = food.find_element(By.CSS_SELECTOR,".common_sp_caption_tit.line2").text
    url = food.find_element(By.CSS_SELECTOR,f"#contents_area_full > ul > ul > li:nth-child({j}) > div.common_sp_thumb > a").get_attribute('href')
    print(name,url)
    j = j+1

imgs = driver.find_elements(By.CSS_SELECTOR,".common_sp_thumb")
i = 1
for img in imgs :
    imgUrl = img.find_element(By.XPATH,f"//*[@id=\"contents_area_full\"]/ul/ul/li[{i}]/div[1]/a/img").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, path + str(count) +".jpg")
    count= count+1
    i = i+1




