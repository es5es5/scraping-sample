from lib2to3.pgen2 import driver
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = 'https://search.naver.com/search.naver?where=news&query=%ED%81%AC%EB%A0%88%EB%B2%84%EC%8A%A4&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0'

# 웹드라이버 설정
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')

driver = webdriver.Chrome('c:/Users/hwlee/Desktop/lhw/chromedriver.exe', options=chrome_options)
driver.implicitly_wait(2)
driver.get(URL)
