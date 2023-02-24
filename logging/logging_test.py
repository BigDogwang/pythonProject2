import logging

#时间格式
#     %(asctime)s输出当前时间
#     %(msg)s  输出打印信息
#     %(name)s  输出名字信息
fmt = "%(name)s--->%(msg)s--->%(asctime)s"
logging.basicConfig(level="DEBUG",format=fmt)

logging.debug('这是debug信息')
logging.info('这是info信息')
logging.warning('这是warning信息')
logging.error('这是error信息')
logging.critical('这是critical信息')

