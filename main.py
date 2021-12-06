import selenium
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito") # 시크릿 창으로 실행

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://classroom.google.com/u/1/c/Mjc1OTgzODcyNTU1') # 클래스룸 입장
driver.maximize_window() # 페이지 전체 화면
time.sleep(7)

driver.find_element_by_name('identifier').send_keys(
    '') # 구글 아이디 입력
driver.find_element_by_css_selector(
    '#identifierNext > div > button > span').click()
time.sleep(5)

driver.find_element_by_name('password').send_keys(
    '') # 구글 비밀번호 입력
driver.find_element_by_css_selector(
    '#passwordNext > div > button > span').click()
time.sleep(10)

driver.find_element_by_css_selector(
    '#ow47 > div:nth-child(2) > div:nth-child(1) > div.n4xnA > div').click() # 출첵 문항 찾기
time.sleep(5)

driver.find_element_by_css_selector(
    '#yDmH0d > div.v7wOcf.ZGnOx > div > div:nth-child(4) > div.fJ1Vac > div.EE538 > div.GWZ7yf.AJFihd.LBlAUc.YkTkoe > div:nth-child(2) > div.lLfZXe.fnxRtf > span > label > div > div > div.vd3tt > div').click()
time.sleep(5) # 출첵 버튼 클릭

driver.find_element_by_css_selector(
    '#yDmH0d > div.v7wOcf.ZGnOx > div.P8NvNd.kdAl3b > div:nth-child(4) > div.fJ1Vac > div.EE538 > div.GWZ7yf.AJFihd.LBlAUc.YkTkoe > div:nth-child(2) > div.heSgkb > div.uArJ5e.UQuaGc.Y5sE8d.CG2qQ.asCVDb').click()
time.sleep(5) # 제출 버튼 클릭

driver.find_element_by_css_selector(
    '#yDmH0d > div.NBxL9e.iWO5td > div > div.I7OXgf.zziILd.ZEeHrd.Inn9w.iWO5td > div.OE6hId.J9fJmf > div.uArJ5e.UQuaGc.kCyAyd.l3F1ye.ARrCac.HvOprf.evJWRb.M9Bg4d').click()
time.sleep(5) # 완료 버튼 클릭

driver.quit() # 드라이버 종료

print("Done")