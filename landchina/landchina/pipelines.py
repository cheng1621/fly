# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
from collections import OrderedDict
from .StoreInMongoDB import MonQueue
class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        print("JsonWithEncodingPipeline closed")
        self.file.close()

    def open_spider(self, spider):
        print("JsonWithEncodingPipeline opend")


class JsonWithEncodingPipeline1(object):

    def __init__(self):
        self.file = codecs.open('info.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        print("JsonWithEncodingPipeline1 closed")
        self.file.close()

    def open_spider(self, spider):
        print("JsonWithEncodingPipeline1 opend")

class MonDBPipeline(object):
    def __init__(self):
        self.queue = MongoQueue('landchina','land')    # create a database and a collection.

    def process_item(self, item, spider):
        self.queue.push(item)
        return item

    def close_spider(self, spider):
        print("MongoDBPipeline closed")

    def open_spider(self, spider):
        print("MongoDBPipeline opend")