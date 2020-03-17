# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals


import json
import codecs
from collections import OrderedDict
import time


class SiweiPipeline(object):
    def __init__(self):
        t = time.localtime()
        f = 'data/' + str(t.tm_hour) + '_' + str(t.tm_min) + '.json'
        self.file = codecs.open(f, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

class lPipeline(object):
    def __init__(self):
        self.file = codecs.open('base.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()