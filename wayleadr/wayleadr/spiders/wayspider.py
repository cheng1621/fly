import scrapy
import json
import sys
from urllib.parse import urlencode
import time
from scrapy.exceptions import CloseSpider
from lxml import etree
class WayspiderSpider(scrapy.Spider):
    name = 'wayspider'
    allowed_domains = ['hotjar.com']
    # start_urls = ['https://in.hotjar.com/api/v2/client/sites/2962848/visit-data?sv=7','https://ws40.hotjar.com/api/v2/sites/2962848/recordings/content']
    start_urls = ['https://app.wayleadr.com/companies/uber/offices/1455-3rd-street-san-francisco-ca/request/new?instant_booking=true',
                  'https://app.wayleadr.com/users/sign_in']
    request_urls = ['https://app.wayleadr.com/companies/uber/offices/1455-3rd-street-san-francisco-ca/request']
    cookies = {}
    def start_requests(self):
        with open('cookie', 'r') as f:
            cookie = f.readline()
        cookies_dict = {str.strip(i.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in cookie.split('; ')}
        self.cookies = cookies_dict

        yield scrapy.Request(url=self.start_urls[0],method='GET',cookies=cookies_dict,dont_filter=True,callback=self.parse)
    def callLogin(self, response):
        result = response.css('form').getall()
        # print(result)
        count = 0

        for i in result:
          if "Unavailable" in i:
            count = count + 1
        if count == 0:
            yield scrapy.Request(url=self.start_urls[1],method='GET',cookies=self.cookies,dont_filter=True,callback=self.parse)
        pass
    def parse(self, response):
        # print(response.text)
        result = response.css('form').getall()
        count = 0

        for i in result:
            if "Unavailable" in i:
                count = count + 1
        if count != 0:
            html1 = etree.HTML(response.text)
            token = html1.xpath('//meta[@name="csrf-token"]/@content')[0]
            # response.body.decode(response.encoding)
            # response.selector.xpath('//small mr-2/text()')
            # data = {'authenticity_token':token}
            yield scrapy.Request(url=self.request_urls[0],
                                 method='POST',
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                 # body=urlencode(data),
                                 cookies=self.cookies,
                                 dont_filter=True,
                                 callback=self.parse1)
        pass

    def parse1(self,response):
        html1 = etree.HTML(response.text)
        token = html1.xpath('//meta[@name="csrf-token"]/@content')[0]
        data = {'authenticity_token': token,
                'booking_request[date_range]':'09/24/2023',
                'booking_request[start_time]':'2023-09-24 01:00:00 -0700',
                'booking_request[end_time]':'2023-09-24 23:30:00 -0700',
                'booking_request[preferred_zone_id]':'1499',
                'booking_request[vehicle_plate]': '45618',
                'booking_request[instant_booking]':'false',
                'booking_request[booking_request_method]':'instant',
                'commit': 'Book Now!',
                'for_user': ''}
        # print(data)
        yield scrapy.Request(url=self.request_urls[0],
                         method='POST',
                         headers={'Content-Type': 'application/x-www-form-urlencoded'},
                         body=urlencode(data),
                         cookies=self.cookies,
                         dont_filter=True,
                         callback=self.parse2)
        pass
    def parse2(self, response):
        print(response.text)
        return {}
