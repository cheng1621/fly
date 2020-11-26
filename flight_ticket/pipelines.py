# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import smtplib
from email.mime.text import MIMEText
from email.header import Header
class FlightPipeline(object):
    def __init__(self):
        # 第三方 SMTP 服务
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_user = "280889477@qq.com"  # 用户名
        self.mail_pass = ""  # 去邮箱获取口令

        self.sender = '280889477@qq.com'
        self.receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    def process_item(self, item, spider):
        message = MIMEText(str(item), 'plain', 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 587)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
        return item
