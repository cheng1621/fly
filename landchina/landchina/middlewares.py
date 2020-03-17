# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from .agent import user_agents
import random
import time
class CookieMiddleware(object):
    def process_request(self,request,spider):
        cookies = {}
        # request.headers['User-Agent'] = random.choice(user_agents)
        request.headers['User-Agent'] ="Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko Core/1.63.6821.400 QQBrowser/10.3.3040.400"
        request.headers['Accept-Language'] = 'zh-CN'
        request.headers['Accept'] = 'text/html, application/xhtml+xml, image/jxr, */*'
        request.headers['Connection'] = 'Keep-Alive'
        # cookies['srcurl'] = '687474703a2f2f7777772e6c616e646368696e612e636f6d2f64656661756c742e617370783f74616269643d323633'
        cookies['Hm_lvt_83853859c7247c5b03b527894622d3fa'] = '1552614268,1552614715,1552870577,1553043166'
        cookies['Hm_lpvt_83853859c7247c5b03b527894622d3fa'] = int(time.time())
        cookies['yunsuo_session_verify'] = 'd04138a022e011754d7f148c17f2c13b'
        cookies['security_session_mid_verify'] = '9554352d98e495828380007a63f29b22'
        cookies['ASP.NET_SessionId'] = 'diejmioel0fepq0n5np43zkv'
        request.cookies = cookies
    def process_response(self,request,response,spider):
        return response
