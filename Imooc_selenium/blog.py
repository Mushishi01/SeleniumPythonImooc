#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.minimize_window()
driver.set_window_size('100','200')
driver.refresh()
driver.back()
driver.forward()