#coding:utf-8
#__author = 'zd'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import config as cf

import sys
sys.path.append("..")
from config.config import *

#发送报告
def send_report():
    msg = MIMEMultipart()#混合格式的邮件
    #邮件正文
    body = MIMEText('测试报告','html','utf-8')
    #某个方法的参数时用utf-8，在pymysql连接时，用utf8
    msg.attach(body)
    #邮件头
    msg['From'] = cf.sender
    msg['To'] = cf.receiver
    msg['Subject']  = cf.subject
    #报告附件'
    with open(cf.report_file,'rb') as f:
        att_file = f.read()
    att1 = MIMEText(att_file,'base64','utf-8')#base64是文件的输出流格式
    att1["Content-Type"] = 'application/octet-stream'#文件发送流格式
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)#Disposition是附件，filename="report.html"是附件名
    msg.attach(att1)#把整个附件添加到报告里
    #发送邮件
    smtp = smtplib.SMTP_SSL(cf.smtp_server)
    smtp.login(cf.smtp_user,cf.smtp_password)
    smtp.sendmail(cf.sender,cf.receiver,msg.as_string())
    cf.logging.info("send email done")

    if __name__ == "__main__":
        send_report("report.html")




# print("发送完成")

# #练习4
# #添加附件的方式
# def send_email2(report_file):
#     msg = MIMEMultipart()
#
#     msg.attach(MIMEText(email_body,'plain','utf-8'))
#     msg['From'] = sender
#     msg["To"] = receiver
#     msg['Subject'] = subject
#
#     with open("report.html",'rb') as f:
#         att1_body = f.read()
#
#     att1 = MIMEText(email_body,'base64','utf-8')#base64是文件的输出流格式
#     att1["Content-Type"] = 'application/octet-stream'#文件发送流格式
#     att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)#Disposition是附件，filename="report.html"是附件名
#     msg.attach(att1)
#
#     smtp = smtplib.SMTP(smtp_server)
#     smtp.login(sender,smtp_password)
#     #smtp.sendmail("test_results@sina.com",'superhin@foxmail.com',msg.as_string())
#     smtp.sendmail(sender,receiver,msg.as_string())
#     smtp.quit()
#
#     print("发送成功")
