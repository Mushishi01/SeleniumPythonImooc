#coding=utf-8
import sys
sys.path.append('E:\\Teacher\\Imooc\\SeleniumPython')
import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import HTMLTestRunner
import unittest
import os
import time


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info("this is chrome")
        
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:
              if error:
                  case_name = self._testMethodName
                  file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                  self.driver.save_screenshot(file_path)
        #print("这个是case的后置调键1")
        self.driver.close()
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
    
    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34@qq.com','user111@qq.com','111111','test1')
        return self.assertFalse(email_error,"测试失败")
        
    def test_login_username_error(self):
        username_error = self.login.login_name_error('111@qq.com','ss','111111','test1')
        self.assertFalse(username_error)

    def test_login_code_error(self):
        code_error = self.login.login_name_error('111@qq.com','ss222','111111','tst1')
        self.assertFalse(code_error)
    
    def test_login_password_error(self):
        password_error = self.login.login_name_error('111@qq.com','ss222','111111','tst1')
        self.assertFalse(password_error)

    def test_login_success(self):
        success = self.login.user_base('111@qq.com','ss222','111111','tst1')
        self.assertFalse(success)
        #self.assert

'''    
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report",description=u"这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)