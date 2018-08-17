#coding=utf-8
import logging
import os
import datetime

class UserLog(object):

    def __init__(self):
        self.logger1 = logging.getLogger(__name__)
        logging.Logger.manager.loggerDict.pop(__name__)
        self.logger1.handlers=[]
        self.logger1.removeHandler(self.logger1.handlers)
        if not self.logger1.handlers:

            self.logger1.setLevel(logging.DEBUG)
            #控制台输出日志
            #consle = logging.StreamHandler()
            #logger.addHandler(consle)

            #文件名字
            base_dir = os.path.dirname(os.path.abspath(__file__))
            log_dir = os.path.join(base_dir,"logs")
            log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
            log_name = log_dir+"/"+log_file
            print(log_name)
            #文件输出日志
            self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
            self.file_handle.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
            self.file_handle.setFormatter(formatter)
            self.logger1.addHandler(self.file_handle)


    def get_log(self):
        return self.logger1
        
    
    def close_handle(self):
        self.logger1.removeHandler(self.file_handle)
        self.file_handle.close()
        


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()
