import logging
import os

# cur = os.path.dirname(__file__)
# log_path = os.path.join(cur,'../logging/2023-1-2.log')
class Log_utils():
    #构造函数
    def __init__(self):#logpath=log_path
        # self.log_path=logpath
        #构建日志器
        self.logger = logging.getLogger()#__name__
        self.logger.setLevel(level=10)

        con = logging.StreamHandler()
        con_1 = "%(name)s--->%(levelname)s--->%(message)s--->%(asctime)s"
        fmt1 = logging.Formatter(fmt=con_1)
        con.setFormatter(fmt1)
        self.logger.addHandler(con)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)

log = Log_utils()
