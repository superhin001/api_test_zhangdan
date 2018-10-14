#coding:utf-8
#__author = 'zd'
import xlrd
import os
import sys
sys.path.append("..")
from config import config as cf


#练习1
#从excel中获取一行用例的数据
#data_file:数据文件；sheet:所在表明；case_name:用例名称
def get_case_data(data_file,sheet,case_name):
    data_file_path = os.path.join(cf.data_file,data_file)
    wb = xlrd.open_workbook(data_file_path)#打开excel
    sh = wb.sheet_by_name(sheet)
    for i in range(1,sh.nrows): #[1,3) 即取值为：1,2
        if sh.cell(i,0).value == case_name:
           return sh.row_values(i)



#
# print(sheet.nrows)
# print(sheet.ncols)
#
##练习2
# #练习：打印excel所有单元格的数据
# for i in  range(0,sheet.nrows):
#     for j in range (0,sheet.ncols):
#         print(sheet.cell(i,j).value)
# #一整行的所有数据
# print(sheet.row_values(0))
#
# #输出所有行的数据
# for i in range(sheet.nrows):
#    print(sheet.row_values(i))
#
# #练习3，找出用例名为test_user_login_normal的数据
#
# for i in range(1,sheet.nrows):
#     if sheet.cell(i,0).value == 'test_user_login_normal':
#         print(sheet.row_values(i))
# #练习4，返回excel中的所有数据

# def excel_to_list(data_file,sheet_name):
#     excel = xlrd.open_workbook(data_file)#打开一个excel
#     sheet = excel.sheet_by_name(sheet_name)#定位一个sheet
#     result = [] #定义一个空列表，以便返回的数据存入
#
#     for i in range(1,sheet.nrows):#从1开始，是因为第一行是说明，无需存入
#         result.append(sheet.row_values(i))#append 是添加的意思
#     return result#把返回的结果都放到列表中，会有2条数据被存入到result中
#
# # #从一张工作表中查找某一条用例的数据,需以excel_to_list为前提
# def  get_test_data(data_list,case_name):#data_list就是上面result中返回的结果，case_name是用例名
#     for case_data in data_list:#case_data是一个变量，这个变量是什么，后面就return什么；data_list是一个列
#         if case_data[0] == case_name:#指定第一行，case_data中有2行数据，我们要的是一行
#             return case_data

# #练习5，从Excel里读取一条用例的数据
# def get_data(file,sheet_name,case_name):
#     wb = xlrd.open_workbook(file)#1.打开一个excel
#     sh = wb.sheet_by_name(sheet_name)#2.定位到一个sheet
#
#     for i in range(1,sh.nrows):
#         if sh.cell(i,0).value == case_name:#从第一行到最后一行遍历
#             return sh.row_values(i)

if __name__== '__main__':
    #练习1
   r = get_case_data("test_user_data.xlsx","TestUserLogin","test_user_login_normal")
    #练习4
    # data_list = excel_to_list('E://Python自动化接口//20180916_zy//data//data.xlsx','TestAddCard')#获取所有数据中的某一条数据
    # print(get_test_data(data_list,'def test_add_card_normal'))

    # #练习5
    # case_data = get_data('../data/data.xlsx','TestAddCard','def test_add_card_normal')
    # print(case_data)#数据名
    # url = case_data[1]#第2列
    # data = case_data
    # expect_res = case_data[4]
    # print(url)
    # print(data)
    # print(expect_res)


