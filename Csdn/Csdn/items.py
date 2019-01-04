# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # 修改自己的相
    title = scrapy.Field()
    time=scrapy.Field()
    number=scrapy.Field()
    pass
