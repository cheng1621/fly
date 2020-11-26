# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
import datetime
import json
import time
try:
    true
except:
    true = True
class ModelSpider(CrawlSpider):
    name = 'ceair'
    allowed_domains = ['ceair.com']
    start_urls = ['http://www.ceair.com/booking/new-low-price-calendar!getDynDayLowPriceEc.shtml']

    def start_requests(self):
        with open('ceair_data.txt', 'r') as f:
            data = f.readlines()
        f.close()
        with open('ceair_cookie.txt','r') as f:
            cookie = f.readline()
        f.close()
        cookies_dict = {str.strip(i.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
                        cookie.split('; ')}
        dic_data = ['cond.monthOffSet=0&cond.depCode=YHM&cond.arrCode=SHA&cond.depCityCode=YTO&cond.arrCityCode=SHA&cond.deptAirport=&cond.arrAirport=&cond.trip=OW&cond.goDt=&cond.depDate=2020-07-01&cond.currency=CNY',
                    'cond.monthOffSet=0&cond.depCode=SEL&cond.arrCode=SHA&cond.depCityCode=SEL&cond.arrCityCode=SHA&cond.deptAirport=&cond.arrAirport=&cond.trip=OW&cond.goDt=&cond.depDate=2020-07-01&cond.currency=CNY']
        for j in range(2):
            yield scrapy.Request(self.start_urls[0], method='POST', cookies=cookies_dict, body=dic_data[0])
            yield scrapy.Request(self.start_urls[0], method='POST', cookies=cookies_dict, body=dic_data[1])
            dic_data[0] = dic_data[0].replace('07-01','07-20')
            dic_data[1] = dic_data[1].replace('07-01','07-20')
            time.sleep(0.1)
    def parse(self, response):
        # print(response.text)
        # print(eval(response.text))
        result = eval(response.text)['currentList']
        print(result)
        for i in range(len(result)):
            temp = result[i]
            if (float(temp['p']) > 0) and (temp['d'] != '2020-06-19'):
                print(float(temp['p']))
                item = temp
                item['air'] = 'ceair'
                return item
