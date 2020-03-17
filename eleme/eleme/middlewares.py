# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class ElemeSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ElemeDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

cookies_dict = {'ubt_ssid': '8bm1ma6gnq2o5953bml3nj1icg2n68fw_2019-01-30',
     '_utrace': '68fb32667178753e6c6306e4f1b03b34_2019-01-30', 'cna': 'nrHOFD6yT18CAXuTx4R/TwmQ', 'UTUSER': '124122888',
     'l': 'bBNtUY8RvHJj2mmTBOCNCZO0fC7OSLAAguWfmHsXi_5Kp6Y_DmQOlkaGwFv6Vj5RsDYB45lflnv9-etk2',
     'eleme__ele_me': '1556b4c747c96de1624f827e7803f92b%3A95a9c2addfff46ca735904c149d9b5c1fd0caf32',
     'track_id': '1550652807|94eae9a939a07d739dc7b701f6be5f525b9111abeba712c10d|ad75d33a9289847f3be3d8eb9d2e8e9a',
     'USERID': '124122888', 'SID': 'vIFfWXDut1SA2avo5HgIs2SREs6Lyi9sGzhg',
     'isg': 'BPLyLXTi-nolBcZgbLWc2_7iQzjez9TBRtlonLzLnKWQT5FJtRIeLKyuP6vWP261',
     # 'pizza73686f7070696e67': 'aDc25_HrnseUqkvJ4FoHbMO6sai0bHIfOXEW5DoKXK9eDkt_lPCob17bOSxmoes3'
    }
class CookiesMiddleware(object):
    def process_response(self,request,response,spider):
        cookies_dict['pizza73686f7070696e67'] = response.headers['Set-Cookie'].decode().split('=')[1].split(';')[0]
        with open("cookies.txt",'r') as f:
            i = f.readlines()[0]
            i = str(int(i) + 24)
        f.close()
        with open("cookies.txt",'w') as f:
            f.write(i)
            f.write('\n')
            f.write(cookies_dict['pizza73686f7070696e67'])
        f.close()
        return response
    def process_request(self,request,spider):
        # print(self.cookies_dict['pizza73686f7070696e67'])
        with open("cookies.txt",'r') as f:
            cookies_dict['pizza73686f7070696e67'] = f.readlines()[1]
        f.close()
        print(cookies_dict['pizza73686f7070696e67'])
        request.cookies = cookies_dict