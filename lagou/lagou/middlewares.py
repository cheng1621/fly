# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import time
from .agents import AGENTS_ALL,user_agents
import logging as log
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.downloadermiddlewares import retry
from scrapy.utils.response import response_status_message
import scrapy
class CookieMiddleware(object):
    def process_request(self,request,spider):

        # with open('111.txt','r') as f:
        #     Cookie = f.read()
        # f.close()
        # cookies_dict = {str.strip(i.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in Cookie.split('; ')}
        cookies_dict = {}
        request.headers['User-Agent'] = random.choice(user_agents)
        # request.headers['User-Agent'] ="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6821.400 QQBrowser/10.3.3040.400"
        cookies_dict['Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6'] = int(time.time())
        cookies_dict['gate_login_token'] = '0168731fe2c3c46110e2c04abdd3d366106b557fb104b5d2d5bbbf8222095d97'
        cookies_dict['unick'] = '%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B70371'
        cookies_dict['login'] = 'true'
        cookies_dict['_putrc'] = '56AB2534C24ECAC3123F89F2B170EADC'
        cookies_dict['user_trace_token'] = '20190307160606-dbdd11be-40af-11e9-8b4b-5254005c3644'
        request.cookies = cookies_dict
    def process_response(self,request,response,spider):
        print(response.headers)
        return response

class ProxyMiddleware(object):
    def __init__(self):
        scrapy.Request('http://39.100.103.134:8888')

    def process_request(self, request, spider):
        # TODO implement complex proxy providing algorithm
        if self.use_proxy(request):
            try:
                request.meta['proxy'] = "http://%s" % random.choice(random.choice(self.p)['IP'])
                # request.meta['proxy'] = "http://122.141.74.186:8080"
            except Exception as e:
                #log.msg("Exception %s" % e, _level=log.CRITICAL)
                log.critical("Exception %s" % e)

    def use_proxy(self, request):
        return True
    def get_proxy_pool(self):
        return self.p

class MyRetryMiddleware(RetryMiddleware):
    logger = log.getLogger(__name__)

    # def delete_proxy(self, proxy):
    #     if proxy:
            # delete proxy from proxies pool

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
                and not request.meta.get('dont_retry', False):
            print(request.meta['proxy'])
            # 删除该代理
            # self.delete_proxy(request.meta.get('proxy', False))
            request.meta['proxy'] = "http://%s" % random.choice(random.choice(ProxyMiddleware().get_proxy_pool())['IP'])
            return self._retry(request, exception, spider)
