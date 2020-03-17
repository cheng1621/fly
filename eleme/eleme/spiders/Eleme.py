from scrapy.spiders import CrawlSpider
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.selector import Selector
import re

import json
import codecs
from collections import OrderedDict
import time
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.http.cookies import CookieJar

from ..items import *
try:
    false,true
except:
    false = False
    true = True

start_urls_base = [
    "https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wm7b2wk0nzvu&" + \
    "latitude=29.60957&limit=24&longitude=106.551201&terminal=web&offset="
]

# cookie = 'ubt_ssid=8bm1ma6gnq2o5953bml3nj1icg2n68fw_2019-01-30; \
#             _utrace=68fb32667178753e6c6306e4f1b03b34_2019-01-30; \
#             cna=nrHOFD6yT18CAXuTx4R/TwmQ; \
#             UTUSER=124122888; l=bBNtUY8RvHJj2mmTBOCNCZO0fC7OSLAAguWfmHsXi_5Kp6Y_DmQOlkaGwFv6Vj5RsDYB45lflnv9-etk2; \
#             eleme__ele_me=1556b4c747c96de1624f827e7803f92b%3A95a9c2addfff46ca735904c149d9b5c1fd0caf32; \
#             track_id=1550652807|94eae9a939a07d739dc7b701f6be5f525b9111abeba712c10d|ad75d33a9289847f3be3d8eb9d2e8e9a; \
#             USERID=124122888; SID=vIFfWXDut1SA2avo5HgIs2SREs6Lyi9sGzhg; \
#             isg=BPLyLXTi-nolBcZgbLWc2_7iQzjez9TBRtlonLzLnKWQT5FJtRIeLKyuP6vWP261; \
#             pizza73686f7070696e67=aDc25_HrnseUqkvJ4FoHbMO6sai0bHIfOXEW5DoKXK9eDkt_lPCob17bOSxmoes3'
#
# cookies_dict = {str.strip(i.split('=')[0]): str.strip(i.split('=')[1]) for i in cookie.split('; ')}
class ElemeSpider(CrawlSpider):
    name = "eleme"
    allowed_domains = ["ele.me"]
    start_urls = [
        "https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wm7b2wk0nzvu&" + \
        "latitude=29.60957&limit=24&longitude=106.551201&offset=24&terminal=web"
    ]
    # rules = [
    #     Rule(sle(allow=("https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wm7b2wk0nzvu&" + \
    #     "latitude=29.60957&limit=24&longitude=106.551201&terminal=web&offset=")), callback='parse', follow=True)
    # ]
    headers = {
    'Accept': 'application/json,text/plain,*/*',
    'referer': 'https://www.ele.me/place/wm7b2wspq0gg?latitude=29.61215&longitude=106.551166',
    'user-agent': 'Mozilla/5.0(Windows NT 10.0; \
    WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 63.0.3239.26 Safari / 537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400',
    'x-shard': 'loc = 106.551166, 29.61215'
    }
    url = start_urls[0]
    def start_requests(self):
        with open("cookies.txt",'r') as f:
            i = f.readlines()[0].strip('\n')
            print(i)
        f.close()
        url = start_urls_base[0] + i
        # print(cookies_dict['pizza73686f7070696e67'])
        # yield scrapy.Request(self.url,cookies=cookies_dict,headers=self.headers,meta={'cookiejar':1})
        yield scrapy.Request(url, headers=self.headers,dont_filter=True)

    def parse1(self,response,Item_class):
        x = eval(response.text)
        Item = Item_class()
        def search(response):
            t = []
            for i in range(len(eval(response.text))):
                Item['ID'] = x[i]['id']
                Item['ComID'] = x[i]['authentic_id']
                Item['Name'] = x[i]['name']
                #Item['tag'] = x[i]['']
                Item['StartPrice'] = x[i]['float_minimum_order_amount']
                Item['score'] = x[i]['rating']
                Item['ServiceScore'] = x[i]['rating']
                Item['FoodScore'] = x[i]['rating']
                Item['SaleTime'] = x[i]['opening_hours']
                # Item['others'] = x[i]['supports'][0]['description']
                Item['notice'] = x[i]['promotion_info']
                a = Item.copy()
                t.append(a)
            return t
        return search(response)
    def parse(self, response):
        x = self.parse1(response, ElemeBaseItem)
        print(x)
        yield OrderedDict(x)
        # print(response.headers['Set-Cookie'].decode().split('=')[1].split(';')[0])
        # cookies_dict['pizza73686f7070696e67'] = response.headers['Set-Cookie'].decode().split('=')[1].split(';')[0]
        # print(cookies_dict)
        with open("cookies.txt",'r') as f:
            i = f.readlines()[0].strip('\n')
        f.close()
        url = start_urls_base[0] + i
        if int(i) < 1000:
            yield scrapy.Request(url, headers=self.headers,callback=self.parse)
        # x = self.parse1(response, ElemeBaseItem)
