#coding:utf-8
#__author = 'zd'
import  unittest
import requests
import json

from lib.read_excel import get_case_data
import sys
sys.path.append("..\...")
from config.config import *
from config import config as cf



#备注：一次只能执行一个用例
class TestUserLogin(unittest.TestCase):
    def test_user_login_normal(self):
        case_data = get_case_data("test_user_data.xlsx",
                                    'TestUserLogin',
                                    'test_user_login_normal')
        # print(case_data)#打印数据名

        url = case_data[1]#第2列
        # print(case_data[3])
        data = (case_data[3])#第4列
        # print(type(case_data[3]))
        expect_res = case_data[4]
        data_dict = json.loads(data)
        print(data_dict)
        res = requests.post(url = url,data = data_dict)

        self.assertEqual(expect_res,res.text)


      #   logging.info("测试用例:{}".format("def test_add_card_normal"))
      #   logging.info("url:{}".format(url))
      #   logging.info("请求数据:{}".format(data))
      #   logging.info("期望结果:{}".format(expect_res))
      #
      #
      #
      # # 发送请求
      #   res = requests.post(url=url, data=data)
      #   print(res.text)

      # 断言
        self.assertEqual(res.text, expect_res)

    # def test_cardNumber_reg_exist(self):
    #     #用例数据
    #     case_data = get_data(data_file,'TestAddCard','def test_cardNumber_reg_exist')
    #     print(case_data)#打印数据名
    #     url = case_data[1]#第2列
    #     data = case_data[3]
    #     #data = json.loads(case_data[3])
    #     expect_res = case_data[4]
    #
    #     logging.info("测试用例:{}".format("def test_cardNumber_reg_exist"))
    #     logging.info("url:{}".format(url))
    #     logging.info("请求数据:{}".format(data))
    #     logging.info("期望结果:{}".format(expect_res))
    #
    #
    #     # url = "http://115.28.108.130:5000/api/user/login/"
    #     # data = {"name":"张三","password":"1234567"}
    #     # #res = requests.post(url=self.url,data=data)#data既可以传文本，又可以传字典，这里json=data也对
    #     # except_res = '<h1>"code":5000,"msg":"该卡已添加","success":false</h1>'
    #     # #self.assertIn("该卡已添加","添加失败，该卡已添加")
    #
    #   # 发送请求
    #     res = requests.post(url=url, data=data)
    #      #res = requests.post(url=url, json=data)，与上面data = json.loads(case_data[3])搭配
    #
    #   # 断言
    #     self.assertEqual(res.text, expect_res)
    #
