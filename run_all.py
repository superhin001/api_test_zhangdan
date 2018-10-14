#coding:utf-8
#__author = 'zd'
"""执行所有用例入口文件"""

import unittest
from config import config as cf
from lib.send_email2 import send_report
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from config.config import *

suite = unittest.defaultTestLoader.discover(cf.testcase_path)
with open(cf.receiver,'wb') as f:#wb是二进制写的格式
    HTMLTestRunner(stream=f,
                   title='api test',
                   description='test').run(suite)

logging.info("="*25+"测试开始"+"="*25)
suite = unittest.defaultTestLoader.discover("./")

with open("report.html","wb") as f:
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述").run(suite)


send_email2("report.html")
logging.info("邮件已发送")
logging.info("="*25+"测试结束"+"="*25)




