# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    chapter = scrapy.Field()
    chapterName = scrapy.Field()
    link = scrapy.Field()
    pass
