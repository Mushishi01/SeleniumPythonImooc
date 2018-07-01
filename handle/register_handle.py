#coding=utf-8
from page.register_page import RegisterPage
import sys
class RegisterHandle(object):
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)
    
    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)

    #输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    
    #输入验证码
    def send_user_code(self,code):
        self.register_p.get_code_element().send_keys(code)
    
    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text
            elif info == 'password_error':
                text = self.register_p.get_password_element().text
            else:
                text = self.register_p.get_code_element().text
        except:
            text = None     
        return text
    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()
    
    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text


        