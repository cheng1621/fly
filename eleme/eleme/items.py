# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class ElemeBaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = Field()    # 编号   type : int
    ComID = Field() # 商户编号 type : varchar
    Name = Field()  # 商户名称 type : varchar
    tag = Field()  # 所属类别  type : varchar
    StartPrice = Field()  # 起送加格 type : int
    score = Field()  # 综合评价分数  type : double
    ServiceScore = Field()  # 服务评价 type:double
    FoodScore = Field()  # 菜品评价  type :double
    SaleTime = Field()  # 营业时间   type: varchar
    others = Field()  # 备注    type : varchar
    notice = Field()  # 公告    type : varchar
    pass

class ElemeLocItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = Field()    # 编号  type : int
    Lon = Field()     # 经度 type : double
    Lat = Field()     # 纬度 type :double
    Loc = Field()     # 商家地址 varchar
    pass

class ElemeEvaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = Field()    # 编号  type : int
    ComID = Field()  # 商户编号 type :varchar
    TimeAvg = Field() # 平均送达时间 type: int
    feeMin = Field()  # 配送费 type: double
    feeMax = Field()  # 最高配送费 type：double
    IsOn = Field()    # 是否开业 type：bool
    evaluate = Field() # 评价    type：int
    ok = Field()      # 满意    type：int
    NotOk = Field()   # 不满意  type：int
    star = Field()    # 星星总数 type：int
    picture = Field() # 返图评价数 type：int
    Number = Field()  # 商户菜品数 type：int
    Sale = Field()    # 月销量    type：int
    time = Field()    # 更新时间  type：char(16)
    pass