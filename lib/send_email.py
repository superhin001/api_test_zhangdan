#coding:utf-8
#__author = 'zd'

import smtplib
from email.mime.text import MIMEText
#1.编写email正文 MILE
msg = MIMEText('这是一封Python发送的邮件','plain','utf-8')#msg是MIMEText格式的对象
#2.编写email头
msg['From'] = "ivan-me@163.com"#用来组装email的文本，无实际用途
msg['To'] = '329133743@qq.com'
msg['Subject'] = "测试报告"
#3.连接smtp服务器，发送邮件
smtp = smtplib.SMTP("smtp.163.com")#.SMTP()适用于http协议;.SMTP_SSL()适用于https协议;
smtp.login("ivan-me@163.com","hanzhichao123")
smtp.sendmail("ivan-me@163.com","329133743@qq.com",msg.as_string())#发件箱，收件箱，转化为字符串
#smtp.sendmail("tivan-me@163.com","",msg.as_string())
smtp.quit()
print("发送完成")




