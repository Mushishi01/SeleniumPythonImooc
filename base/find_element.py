#coding=utf-8
from util.read_ini import ReadIni
from log.user_log import UserLog
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
        get_user_log = UserLog()
        self.logger = get_user_log.get_log()
    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        self.logger.info("定位方式:"+by+"--->定位值:"+value)
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None