# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import time
import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.header import Header
from scrapy.exceptions import CloseSpider
class WayleadrPipeline:
    def __init__(self):
        # 第三方 SMTP 服务
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_user = "501688324@qq.com"  # 用户名
        self.mail_pass = "bfgjjgsqptfwbjaf"  # 去邮箱获取口令

        self.sender = '501688324@qq.com'
        self.receivers = ['280889477@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    def process_item(self, item, spider):
        # message = MIMEText("gogogo", 'plain', 'utf-8')
        # # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
        # message["From"] = Header("cheng <501688324@qq.com>")
        # message["To"] = Header("456", "utf-8")
        # message["Subject"] = Header("789", "utf-8")
        # try:
        #     smtpObj = smtplib.SMTP()
        #     smtpObj.connect(self.mail_host, 587)  # 25 为 SMTP 端口号
        #     result = smtpObj.login(self.mail_user, self.mail_pass)
        #     print(result)
        #     smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        #     smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        #     smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        #     print("邮件发送成功")
        # except smtplib.SMTPException as e:
        #     print("Error: 无法发送邮件",str(e))
        # os.kill(os.getppid(),9)
        return item
