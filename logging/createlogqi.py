import logging

#1.创建日志对象
logs = logging.getLogger()
logs.setLevel("DEBUG")

#2.创建控制台处理器
#console = logging.StreamHandler()

#创建文件的处理器
console = logging.FileHandler('../logging/logs.txt',mode='a',encoding='utf-8')

#控制台的等级 .setLevel
console.setLevel(level="DEBUG")

#日志器添加控制台处理器
logs.addHandler(console)

logging.debug('这是debug信息')
logging.info('这是info信息')
logging.warning('这是warning信息')
logging.error('这是error信息')
logging.critical('这是critical信息')