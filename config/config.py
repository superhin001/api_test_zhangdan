#coding:utf-8
#__author = 'zd'
"""项目配置文件"""
import logging
import os
#项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#__file_是当前文件，即config.py;os.path.abspath（）是取当前文件的绝对路劲；os.path.dirname（）是（上级）文件夹名；
# 这里整个方法就是一个方法，是为了取到项目的名称。方法从最里层括号，向外依次是：文件config.py，
# 文件的上级文件夹config,文件的上上级文件夹（项目）接口20181014
data_file = os.path.join(prj_path,'data')
#文件夹路径，项目路径上连接一个data目录，拼接成一个新的路径，就是data文件夹
#上面的os.path.join（）方法，相当于C:/api_test/data，但是上面的方法无论是windows还是linx都适用，
#下面的只能单独用于windows或linx，indowsprj_path\data：linx：prj_path/data
testcase_path = os.path.join(prj_path,'testcase')
#同上，也是文件夹路径，相当于prj_path/testcase,prj_path项目，testcase是用例
#windowsprj_path\testcase：linx：prj_path/testcase
print(prj_path)
print(testcase_path)
print(data_file)

report_file = os.path.join(prj_path,'report','report.html')
log_file = os.path.join(prj_path,'log','log.txt')

#全局log（日志）配置
# logging.basicConfig(level=logging.INFO,
#                     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
#                     datefmt="%Y-%m-%d %H:%M:%S",#日期格式
#                     filename=log_file,#日志输出文件
#                     filemode="a")#追加模式

# logging.basicConfig(level=logging.DEBUG,
#                     format='[%(asctime)s]-%(message)s',
#                     datefmt="%Y-%m-%d %H:%M:S",
#                     filename="log.txt",
#                     filemode="a")

#数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'

#邮件配置
smtp_server = 'smtp.sina.com'#smtp服务器地址
smtp_user = 'test_results@sina.com'
smtp_password = 'hanzhichao123'

subject = '接口测试报告'#邮件主题
sender = smtp_user#邮件发送人
receiver = '329133743@qq.com'#邮件接收


is_send_email = False#是否发送邮件开关
#
if __name__ == '__main__':
    print(report_file)
    #logging.info("hello world")



