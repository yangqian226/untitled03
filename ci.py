from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(2)
driver.get('http://www.baidu.com')

print('222')