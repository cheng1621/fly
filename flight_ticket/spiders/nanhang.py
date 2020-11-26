# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
import datetime
import json
import time
try:
    true;false;null
except:
    true = True;false=False;null=None;
class ModelSpider(CrawlSpider):
    name = 'nanhang'
    allowed_domains = ['b2c.csair.com']
    start_urls = ['https://b2c.csair.com/ita/rest/intl/shop/calendar']
    def start_requests(self):
        with open('nanhang_cookie.txt','r') as f:
            cookie = f.readline()
        cookies_dict = {str.strip(i.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
                        cookie.split('; ')}
        for i in range(-21, 1, 3):
            data = 'execution=ae16d8e7a69866aaf0ed248404dea9a6&country=cn&move='
            data = data + str(i) + '&'
            data = data + '_=' + str(int(time.time()))
            print(data)
            yield scrapy.Request(self.start_urls[0],method='GET',cookies=cookies_dict,body=data,dont_filter=true)
            time.sleep(0.1)


    def parse(self, response):
        print(response.text)
        result = eval(response.text)['ita']['calendar']
        print(result)