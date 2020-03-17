# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LandchinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    pass

class LandItem(scrapy.Item):
    ID = scrapy.Field()
    SuperviseId = scrapy.Field()
    district = scrapy.Field()
    name = scrapy.Field()
    Lon = scrapy.Field()
    Lat = scrapy.Field()
    Loc = scrapy.Field()
    area = scrapy.Field()
    source = scrapy.Field()
    purpose = scrapy.Field()
    supply = scrapy.Field()
    industry = scrapy.Field()
    level = scrapy.Field()
    owner = scrapy.Field()
    TimeDeliver = scrapy.Field()
    TimeBegin = scrapy.Field()
    TimeOver = scrapy.Field()
    sanction = scrapy.Field()
    TimeContract = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()

