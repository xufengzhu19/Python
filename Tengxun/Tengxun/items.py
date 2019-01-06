# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    jobName = scrapy.Field()
    jobCategory = scrapy.Field()
    jobNumber = scrapy.Field()
    jobAddress = scrapy.Field()
    pubTime = scrapy.Field()
    jobLink = scrapy.Field()
    pass
