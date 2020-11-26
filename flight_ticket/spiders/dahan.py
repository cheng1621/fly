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
    name = 'dahan'
    allowed_domains = ['koreanair.com']
    start_urls = ['https://www.koreanair.com/api/fly/revenue/from/LAX/to/SEL/on/05-29-2020-0000']

    def start_requests(self):
        parse_url = self.start_urls[0]
        # data = 'flexDays=30&scheduleDriven=false&purchaseThirdPerson=&domestic=false&isUpgradeableCabin=false&currency=USD&bonusType=SKYPASS&countryCode=&adults=1&children=0&infants=0&cabinClass=ECONOMY&adultDiscounts=&adultInboundDiscounts=&childDiscounts=&childInboundDiscounts=&infantDiscounts=&infantInboundDiscounts=&_=1589273474987'
        data = 'flexDays=0&scheduleDriven=false&purchaseThirdPerson=&domestic=false&isUpgradeableCabin=false&currency=USD&bonusType=SKYPASS&countryCode=&adults=1&children=0&infants=0&cabinClass=ECONOMY&adultDiscounts=&adultInboundDiscounts=&childDiscounts=&childInboundDiscounts=&infantDiscounts=&infantInboundDiscounts=&_=1589993301603'
        with open('dahan_cookie.txt','r') as f:
            cookie = f.readline()
        cookies_dict = {str.strip(cookie.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
                        cookie.split('; ')}
        yield scrapy.Request(parse_url,method='GET',cookies=cookies_dict,body=data,dont_filter=true)


    def parse(self, response):
        print(1)
        print(response)
        print(response.text)