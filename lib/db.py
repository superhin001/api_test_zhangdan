#coding:utf-8
#__author = 'zd'
"""数据库操作"""
import pymysql
import sys
sys.path.append("..")#提升包的搜索路径到项目下。这里是提升一级，提升2级为“../..”。
#因为是从run_all来调用，run_all在项目下，无论哪个文件，我们都从项目下找
from config import config as cf#从config文件夹把包导出来，并为其定义别名
#from config.config import *


# 获取连接方法
#从配置文件中读取我们需要的环境变量
def get_db_conn():
    conn = pymysql.connect(host=cf.db_host,
                           port=cf.db_port,
                           user=cf.db_user,
                           password=cf.db_password,
                           db=cf.db,
                           charset='utf8')
    return conn
#查询操作
def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cf.logging.debug(sql)#查询sql输出到log。debug小写是一个方法，大写是一个数字
    cf.logging.debug(result)#查询结果输出到log
    cur.close()#在执行下面修改等操作前需要将游标及连接关闭，这样好释放内存
    conn.close()
    return result
#修改操作
def change_db(sql):
    cf.logging.debug(sql)
    conn = get_db_conn()
    cur = conn.cursor()
    try:
      cur.execute(sql)
      conn.commit()
    except Exception as e:
         conn.rollback()
         cf.logging.error(str(e))
    finally:
         cur.close()
         conn.close()


# # 封装常用数据库操作
# def check_cardNumber(cardNumber):
#     # 注意sql中''号嵌套的问题
#     sql = "select * from cardinfo where cardNumber = '{}'".format(cardNumber)
#     result = query_db(sql)
#     return True if result else False
#
# def add_cardNumber(cardNumber):
#     sql = "insert into cardinfo (cardNumber) values ('{}')".format(cardNumber)
#     change_db(sql)
#
# def del_cardNumber(cardNumber):
#     sql = "delete from cardinfo where name='{}'".format(cardNumber)
#     change_db(sql)
#
# def check_cardStatus(cardNumber):
#     sql = "select cardstatus from cardinfo where cardnumber={}".format(cardNumber)
#     result = query_db(sql)
#     type(result)
#     print(type(result))
#     if result[0] == 5010:
#         print (result[0])
#         return True
#     else:
#         print(result[0])
#         return False
if __name__ == '__main__':
    result = query_db("select * from user where name = '张三'")
    print(result)
   # print(check_cardNumber('45678'))
  # print(check_cardStatus('20180906003'))


