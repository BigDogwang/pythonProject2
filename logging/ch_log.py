import logging

#第一步：创建日志器
logs = logging.getLogger()
#第二步：定义处理器，控制台输出和文件输出 两种
con = logging.StreamHandler()
file = logging.FileHandler('../logging/cuihao.txt',mode='a',encoding='utf-8')
#第三步：设置不同的输出格式
con_1 = "%(name)s--->%(levelname)s--->%(message)s--->%(asctime)s"
file_1 = "%(asctime)s===>%(name)s===>%(message)s"
#格式
fmt1 = logging.Formatter(fmt=con_1)
fmt2 = logging.Formatter(fmt=file_1)

con.setFormatter(fmt1)
file.setFormatter(fmt2)
#第四步：日志添加处理器
logs.addHandler(con)
logs.addHandler((file))


logs.debug('这是debug信息')
logs.info('这是info信息')
logs.warning('这是warning信息')
logs.error('这是error信息')
logs.critical('这是critical信息')