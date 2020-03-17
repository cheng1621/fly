# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from .agent import user_agents
import random
import scrapy
class CookiessMiddleware(object):
    def process_request(self,request,spider):
        cookies = {}
        with open('flights.txt','r') as f:
            Cookie = f.readline()
        cookies_dict = {str.strip(i.split('=')[0].strip()): str.strip(i.split('=')[1].strip()) for i in
                        Cookie.split('; ')}
        request.cookies = cookies_dict
        request.headers['User-Agent'] = random.choice(user_agents)
        request.headers['content-type'] = 'application/json'
    def process_response(self,request,response,spider):
        return response

