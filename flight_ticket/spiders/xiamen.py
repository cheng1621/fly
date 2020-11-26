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
    name = 'xiamenair'
    allowed_domains = ['xiamenair.com']
    start_urls = ['https://www.xiamenair.com/api/offers']

    def start_requests(self):
        data = '{"ecip":{"shoppingPreference":{"connectionPreference":{"maxConnectionQuantity":2},"flightPreference":{"cabinCombineMode":"Cabin","lowestFare":true},"accountCodeSlogan":""},"cabinClasses":["Economy","Business","First"],"passengerCount":{"adult":1,"child":0,"infant":0},"itineraries":[{"departureDate":"2020-07-04","origin":{"airport":{"code":"ICN"}},"destination":{"airport":{"code":"FOC"}},"segments":[]}]},"jfCabinFirst":false,"dOrI":"I","isJCGM":false}'
        with open('xiamen_cookie.txt','r') as f:
            cookie = f.readline()
        cookies_dict = {str.strip(cookie.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
                        cookie.split('; ')}
        now = datetime.date(2020,7,4)
        end = datetime.date(2020,7,30)
        delta = datetime.timedelta(days=7)
        while now < end:

            yield scrapy.Request(self.start_urls[0],method='POST',cookies=cookies_dict,body=data,dont_filter=true)
            data = data.replace(str(now), str(now + delta))
            now = now + delta
            time.sleep(1)


    def parse(self, response):
        print(response.text)
        result = eval(response.text)['result']
        print(result)
        if result is not None:
            try:
                temp = result['egr']['offerItemCount']
                print(temp)
                item['xiamen'] = 1
                return item
            except:
                pass

