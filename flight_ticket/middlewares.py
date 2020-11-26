# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import scrapy

class CookiessMiddleware(object):
    def process_request(self,request,spider):

        # cookies = {}
        # with open('ceair_cookie.txt','r') as f:
        #     Cookie = f.readlines()
        # f.close()
        # for i in Cookie:
        #     # temp = {str.strip(i.split(': ')[0].strip()): str.strip(i.split(': ')[1].strip())}
        #     temp = str.strip(i.split(': ')[0].strip())
        #     item_temp = str.strip(i.split(':')[1].strip())
        #     if temp != 'Cookie':
        #         continue
        #         request.headers[str.strip(i.split(': ')[0].strip())] = str.strip(i.split(': ')[1].strip())
        #     else:
        #         cookies_dict = {str.strip(i.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
        #                 item_temp.split('; ')}
        # # print(cookies_dict)
        # request.cookies = cookies_dict
        # request.headers['Referer'] = 'http://www.ceair.com/booking/yhm-sha-200619_CNY.html'
        request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        if spider.name is 'xiamenair':
            request.headers['Accept'] = 'application/json, text/plain, */*'
        else:
            request.headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        # request.headers['Accept'] = 'application/json, text/plain, */*'
        # request.headers['Connection'] = 'keep-alive'
        if spider.name is not 'nanhang':
            request.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        # request.headers['Content-Type'] = 'application/json;charset=UTF-8'
        # request.headers['Content-Type'] = 'application/json'
        if spider.name is 'xiamenair':
            request.headers['Accept-language'] = 'zh-cn'
            request.headers['Content-Type'] = 'application/json;charset=UTF-8'
        else:
            request.headers['Accept-language'] = 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
        # request.headers['Accept-Language'] = 'zh-cn'
    def process_response(self,request,response,spider):
        return response
