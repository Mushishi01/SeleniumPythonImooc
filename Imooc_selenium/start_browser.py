#coding=utf-8
from selenium import webdriver
import time
import random
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver2 = webdriver.Firefox()
#driver1 = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
email_element.send_keys('sdfsd')
driver.find_element_by_id('captcha_code').send_keys("test")
print(driver.find_element_by_id('register_email-error').text)
print(driver.find_element_by_id('register_email-error').get_attribute('value'))
#driver.save_screenshot("E:/Teacher/Imooc/imooc2.png")
#code_element = driver.find_element_by_id("getcode_num")
#print(code_element.location)#{"x":123,"y":345}
#left = code_element.location['x']
#top = code_element.location['y']
#right = code_element.size['width']+left
#height = code_element.size['height']+top
#im = Image.open("E:/Teacher/Imooc/imooc2.png")
#img = im.crop((left,top,right,height))
#img.save("E:/Teacher/Imooc/imooc3.png")

#r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
#r.addBodyPara("typeId", "35")
#r.addBodyPara("convert_to_jpg", "0")
#r.addFilePara("image", r"E:/Teacher/Imooc/imooc3.png") #文件上传时设置
#res = r.post()
#text = res.json()['showapi_res_body']['Result']
#print(text) # 返回信息
#time.sleep(2)




#user_email = ''.join(random.sample('1234567890abcdefg',8))+"@163.com"
#print(user_email)




element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

print(email_element.get_attribute("placeholder"))
email_element.send_keys("test@163.com")
print(email_element.get_attribute("value"))
time.sleep(5)
driver.close()



#driver.find_element_by_id("register_email").send_keys("mushishi_01@163.com")
##user_name_element_node =driver.find_elements_by_class_name("controls")[1]
#user_element = user_name_element_node.find_element_by_class_name("form-control")
#user_element.send_keys("qerqewre")
#driver.find_element_by_name("password").send_keys("111111")
#driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")