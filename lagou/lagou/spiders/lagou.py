
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from ..agents import *
import random
class LagouSpider(CrawlSpider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [
        "https://www.lagou.com/"
        # "https://www.ele.me"
    ]
    rules = [
        Rule(sle(allow=(r"/jobs/[0-9]+.html$")),follow = True,callback='parse_1')
    ]

    def parse_1(self,response):
        print(response.status)
    # def parse(self,response):
    #     print(response.url)