

import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.selector import Selector
from..items import LandchinaItem,LandItem
import re
import random
import datetime
import time
from ..StoreInMongoDB import MonQueue
import json
class CommonSpider(CrawlSpider):

    auto_join_text = False

    # Extract content without any extra spaces.
    # NOTE: If content only has spaces, then it would be ignored.
    def extract_item(self, sels):
        contents = []
        for i in sels:
            content = re.sub(r'\s+', ' ', i.extract())
            if content != ' ':
                contents.append(content)

        return contents

    def extract_items(self, sel, rules, item):
        # print(item)
        for nk, nv in rules.items():
            if nk in ('__use', '__list'):
                continue
            if nk not in item:
                item[nk] = []
            if sel.css(nv):
                # item[nk] += [i.extract() for i in sel.css(nv)]
                # Without any extra spaces:
                item[nk] += self.extract_item(sel.css(nv))
                if nk == 'source':
                    if item['area'][0] == item[nk][0]:
                        item[nk] = ['现有建设用地']
                    elif int(float(item[nk][0])) == 0:
                        item[nk] = ['新增建设用地']
                    else:
                        item[nk] = ['新增建设用地(来自存量库)']
            else:
                item[nk] = []

    # 1. item是一个单独的item，所有数据都聚合到其中 *merge
    # 2. 存在item列表，所有item归入items
    def traversal(self, sel, rules, item_class, item, items):
        # print 'traversal:', sel, rules.keys()
        if item is None:
            item = item_class()
        if '__use' in rules:
            if '__list' in rules:
                unique_item = item_class()
                self.extract_items(sel, rules, unique_item)
                items.append(unique_item)
            else:
                self.extract_items(sel, rules, item)
        else:
            for nk, nv in rules.items():
                for i in sel.css(nk):
                    self.traversal(i, nv, item_class, item, items)

    DEBUG=True
    def debug(self, sth):
        if self.DEBUG == True:
            print(sth)

    def deal_text(self, sel, item, force_1_item, k, v):
        if v.endswith('::text') and self.auto_join_text:
            item[k] = ' '.join(self.extract_item(sel.css(v)))
        else:
            _items = self.extract_item(sel.css(v))
            if force_1_item:
                if len(_items) >= 1:
                    item[k] = _items[0]
                else:
                    item[k] = ''
            else:
                item[k] = _items

    keywords = set(['__use', '__list'])
    def traversal_dict(self, sel, rules, item_class, item, items, force_1_item):
        #import pdb; pdb.set_trace()
        item = {}
        for k, v in rules.items():
            if type(v) != dict:
                if k in self.keywords:
                    continue
                if type(v) == list:
                    continue
                self.deal_text(sel, item, force_1_item, k, v)
                #import pdb;pdb.set_trace()
            else:
                item[k] = []
                for i in sel.css(k):
                    #print(k, v)
                    self.traversal_dict(i, v, item_class, item, item[k], force_1_item)
        items.append(item)

    def dfs(self, sel, rules, item_class, force_1_item):
        if sel is None:
            return []
        items = []
        if item_class != dict:
            self.traversal(sel, rules, item_class, None, items)
        else:
            self.traversal_dict(sel, rules, item_class, None, items, force_1_item)
        return items

    def parse_with_rules(self, response, rules, item_class, force_1_item=False):
        return self.dfs(Selector(response), rules, item_class, force_1_item)

class landchinaSpider(CommonSpider):
    name = "landchina"
    allowed_domains = ["landchina.com","restapi.amap.com"]
    start_urls = [
        # "http://www.landchina.com/default.aspx?tabid=263"
        'http://www.landchina.com//default.aspx?tabid=386&comname=default&'+
        'wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&recorderguid=836932ADF0C63246E055000000000001'
    ]

    # rules = [
    #     Rule(sle(allow=(r"/jobs/[0-9]+.html$")),follow = True,callback='parse_1')
    # ]
    list_rule = {
        '.gridItem,.gridAlternatingItem':{
            '__use':'1',
            '__list':'1',
            'url':'a::attr(href)'
        }
    }
    list_rule1 = {
        '__use': '1',
        '__list': '1',
        'url':'.pager::text'
    }
    list_rule2 = {
        '#mainModuleContainer_1855_1856_ctl00_ctl00_vdFromIII':{
            '__use': '1',
            '__list': '1',
            'ID':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl_value::attr(value)',
            'SuperviseId':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c4_ctrl::text',
            'district':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r1_c2_ctrl::text',
            'name':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r17_c2_ctrl::text',
            'Loc':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r16_c2_ctrl::text',
            # 'Lon': '1',
            # 'Lat': '1',
            'area':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c2_ctrl::text',
            'source':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r2_c4_ctrl::text',
            'purpose':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c2_ctrl::text',
            'supply':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r3_c4_ctrl::text',
            'industry':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c4_ctrl::text',
            'level':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c2_ctrl::text',
            'owner':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r9_c2_ctrl::text',
            'TimeDeliver':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r21_c4_ctrl::text',
            'TimeBegin':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c2_ctrl::text',
            'TimeOver':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r22_c4_ctrl::text',
            'sanction':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c2_ctrl::text',
            'TimeContract':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r14_c4_ctrl::text',
            'year':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r19_c2_ctrl::text',
            'price':'#mainModuleContainer_1855_1856_ctl00_ctl00_p1_f1_r20_c4_ctrl::text'
        }
    }
    # def start_requests(self):
    #     now = datetime.date(2015,1,1)
    #     delta = datetime.timedelta(days=1)
    #     # end = time.strftime('%Y-%m-%d')
    #     end = datetime.date(2019,1,1)
    #     while now <= end:
    #         data = {
    #             'TAB_QuerySubmitPagerData': '1',
    #             'TAB_QuerySubmitConditionData': '9f2c3acd-0256-4da2-a659-6949c4671a2a:%s~%s' % (
    #             str(now), str(now))
    #         }
    #         now = now + delta
    #         time.sleep(0.1)
    #         yield scrapy.FormRequest(self.start_urls[0],formdata = data,dont_filter = True)
    def start_requests(self):
        with open('data_utf8.json','r') as f:
            a = f.readline()
            while a != '':
                dic = 'http://www.landchina.com/' + eval(a)['url'][0]
                print(dic)
                a = f.readline()
                yield scrapy.Request(dic,dont_filter = True)
    def parse(self,response):
        # x = self.parse_with_rules(response,self.list_rule,LandchinaItem)
        x = self.parse_with_rules(response, self.list_rule2, LandItem)
        url = u"http://restapi.amap.com/v3/geocode/geo?key=f60e7eca691650c46cc4bd3654b0b844&address=" + x[0]['Loc'][0]
        print(url)
        yield scrapy.Request(url,meta={'item':x[0]},callback = self.parse1)
    def parse1(self,response):
        x = response.meta['item']
        if response.status == 200 and eval(response.text)['status'] == '1':
            try:
                y = eval(response.text)['geocodes'][0]['location'].split(',')
            except:
                y = [[''],['']]
            x['Lon'] = y[0]
            x['Lat'] = y[1]
        else:
            x['Lon'] = []
            x['Lat'] = []
        return x
