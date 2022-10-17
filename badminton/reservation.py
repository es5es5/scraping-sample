import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class TimeOutException(Exception):
    pass

url = 'https://yeyak.seoul.go.kr/web/main.do'
html = requests.get(url)


# 웹드라이버 설정
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
driver = webdriver.Chrome('c:/Users/hwlee/Desktop/lhw/chromedriver.exe', options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get(url)

print(driver.title)


html = driver.page_source

loginBtn = driver.find_element_by_css_selector('#header > div.container > div > div.state > a')
loginBtn.click()

loginId = driver.find_element_by_id('userid')
loginPass = driver.find_element_by_id('userpwd')

print(loginId)
loginId.send_keys('')
loginPass.send_keys('')
loginPass.send_keys(Keys.RETURN)
driver.implicitly_wait(500)

try:
  WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#contents > div > div.main_step.type5 > div > ul > li.quick_reserv > a'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  하이패스 = driver.find_element_by_css_selector('#contents > div > div.main_step.type5 > div > ul > li.quick_reserv > a')
  하이패스.click()



try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#place_code1 > li.svc_T104.svc_img > a'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  print('체육시설_배드민턴장')
  체육시설_배드민턴장 = driver.find_element_by_css_selector('#place_code1 > li.svc_T104.svc_img > a')
  체육시설_배드민턴장.click()

try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#aform > div > div.main_step2 > div > div > div.tab_con.active > ul > li:nth-child(2) > div > div > div > map > area:nth-child(11)'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  print('지역_성동구')
  지역_성동구 = driver.find_element_by_css_selector('#aform > div > div.main_step2 > div > div > div.tab_con.active > ul > li:nth-child(2) > div > div > div > map > area:nth-child(11)')
  지역_성동구.click()
  지역_성동구.click()

try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#svc_list_d > li:nth-child(1) > a:nth-child(1)'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  print('배드민턴장_1번코트')
  배드민턴장_1번코트 = driver.find_element_by_css_selector('#svc_list_d > li:nth-child(1) > a:nth-child(1)')
  배드민턴장_1번코트.click()

try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#calendar_20221024 > a'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  print('달력_날짜')
  달력_날짜 = driver.find_element_by_css_selector('#calendar_20221024 > a')
  달력_날짜.click()

try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#aform > div > div.main_step2 > div > div > div.tab_con.active > div > button'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  print('예약하기')
  예약하기 = driver.find_element_by_css_selector('#aform > div > div.main_step2 > div > div > div.tab_con.active > div > button')
  예약하기.click()


# next_url = driver.current_url
# html = requests.get(next_url)
# # driver.quit()
# driver.switch_to.window(driver.window_handles[-1])

# driver = webdriver.Chrome('c:/Users/hwlee/Desktop/lhw/chromedriver.exe', options=chrome_options)
# driver.maximize_window()
driver.implicitly_wait(4)
# driver.get(next_url)

try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#unit0 > a'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  print('시간대_0')
  시간대_0 = driver.find_element_by_css_selector('#unit0 > a')
  시간대_0.click()

try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.total_agree > span > label'))
  )
except TimeOutException:
    print("타임아웃")
finally:
  print('전체동의')
  전체동의 = driver.find_element_by_css_selector('div.total_agree > span > label')
  전체동의.click()
