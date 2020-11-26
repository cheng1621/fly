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
    name = 'jizhou'
    allowed_domains = ['jejuair.net']
    start_urls = ['https://ibsearch.jejuair.net/jejuair/com/jeju/ibe/availHybris.do']
    Date = ["2020-05-27", "2020-06-03", "2020-06-10", "2020-06-17", "2020-06-24", "2020-07-01"]
    # Date = ["2020-06-16"]
    def start_requests(self):
        parse_url = self.start_urls[0]
        data = 'AdultPaxCnt=1&ChildPaxCnt=0&InfantPaxCnt=0&RouteType=I&Language=CN&ReturnSeatAvail=true&PointsPayment=false&TripType=OW&DepDate=2020-06-09&SegType=DEP&DepStn=ICN&ArrStn=WEH'
        now = datetime.date(2020,7,22)
        data = data.replace('2020-06-09', str(now))
        end = datetime.date(2020,8,30)
        delta = datetime.timedelta(days=7)

        while now < end:
            data = data.replace(str(now),str(now + delta))
            now = now + delta
            with open('jizhou_cookie.txt','r') as f:
                cookie = f.readline()
            cookies_dict = {str.strip(cookie.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
                            cookie.split('; ')}
            yield scrapy.Request(parse_url,method='POST',cookies=cookies_dict,body=data,dont_filter=true)
            time.sleep(0.1)



    def parse(self, response):
        # print(response.text)
        result = eval(response.text)['Result']['Data']['AvailabilityDates']
        # print(result)
        for i in range(len(result)):
            try:
                if result[i]['CheapestPointsFare']:
                    print(result[i]['Date'])
                    print(result[i]['CheapestPointsFare'])
                    return result[i]['Availability']
            except:
                continue



