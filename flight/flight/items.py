# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FlightItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = scrapy.Field()    # 编号
    FDid = scrapy.Field()  # 航班日期编号
    FlightId = scrapy.Field() # 航班号
    StartCity = scrapy.Field() # 出发城市
    ArriveCity = scrapy.Field() # 到达城市
    StartAirport = scrapy.Field() # 出发机场
    ArriveAirport = scrapy.Field() # 类型
    type = scrapy.Field() # 机型
    AirType = scrapy.Field() # 餐食
    food = scrapy.Field() # 起飞准点率
    PunctStratRate = scrapy.Field() # 起飞延误时间
    LateStratTime = scrapy.Field() # 到达准点率
    PunctArriveRate = scrapy.Field() # 到达延误时间
    LateArriveTime = scrapy.Field() # 对应出发日期价格
    price = scrapy.Field() # 对应出发日期价格
    discount = scrapy.Field() # 对应出发日期折扣
    time = scrapy.Field()  # 出发日期
    pass
