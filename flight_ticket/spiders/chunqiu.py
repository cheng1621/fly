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
    name = 'chunqiuair'
    allowed_domains = ['flights.ch.com']
    start_urls = ['https://flights.ch.com/Flights/SearchByTime']

    def start_requests(self):
        data = 'IsShowTaxprice=false&Active9s=&IsJC=false&Currency=0&SType=1&Departure=%E9%A6%96%E5%B0%94&Arrival=%E4%B8%8A%E6%B5%B7&DepartureDate=2020-05-20&ReturnDate=null&IsIJFlight=false&IsBg=false&IsEmployee=false&IsLittleGroupFlight=false&SeatsNum=1&ActId=0&IfRet=false&IsUM=false&CabinActId=null&SpecTravTypeId=&IsContains9CAndIJ=false&isdisplayold=false'
        with open('chunqiu_cookie.txt','r') as f:
            cookie = f.readline()
        cookies_dict = {str.strip(cookie.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
                        cookie.split('; ')}
        now = datetime.date(2020,5,13)
        end = datetime.date(2020,6,30)
        delta = datetime.timedelta(days=1)
        while now < end:
            data = data.replace('05-20',str(now))
            yield scrapy.Request(self.start_urls[0],method='POST',cookies=cookies_dict,body=data,dont_filter=true)
            time.sleep(0.1)

    def parse(self, response):
        result = eval(response.text)['Route']
        print(len(result))
        print(result)
        # send email if length is not equal to 0;

