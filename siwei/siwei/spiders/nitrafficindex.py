
from scrapy.spiders import CrawlSpider
import scrapy
from ..settings import USER_AGENT_LIST
import random
import time
class ZhihuSpider(CrawlSpider):
    name = "nitrafficindex"
    allowed_domains = ["nitrafficindex.com"]
    start_urls = [
        # "http://www.nitrafficindex.com/"
        "http://www.nitrafficindex.com/traffic/getRoadIndex.do"
    ]
    # header = {
    #     'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome /63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400',
    #     # 'Host': 'www.nitrafficindex.com',
    #     # 'Referer': 'http://www.nitrafficindex.com/trafficIndexAnalysis.html',
    #     # 'X-Requested-With': 'XMLHttpRequest',
    #     # 'Accept': 'application/json, text/javascript, */*',
    #     # # 'Content-Type':'application/x-www-form-urlencoded',
    #     # 'Content-Type': 'application/json',
    #     # 'Origin': 'http://www.nitrafficindex.com'
    # }
    header = {'User-Agent':random.choice(USER_AGENT_LIST)}
    def start_requests(self):
        url = self.start_urls[0]
        queryParams = {
            'areaCode': '120000',
            'roadLevel': '1,2,3,4',
            'page': '1',
            'rows': '10000'
        }
        yield scrapy.FormRequest(url = url, formdata=queryParams)
    def parse(self,response):
        a = eval(response.text)['rows']
        return a
        # return eval(response.text)['rows']