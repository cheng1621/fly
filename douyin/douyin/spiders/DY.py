import scrapy


class DySpider(scrapy.Spider):
    name = 'DY'
    allowed_domains = ['douyin.com']
    start_urls = ['https://www.douyin.com/']

    # def start_requests(self):
    #     yield scrapy.Request(dic,dont_filter = True)
    def parse(self,response):
        print(response)