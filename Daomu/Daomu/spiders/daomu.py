# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = "daomu"
    allowed_domains = ["http://www.daomubiji.com"]
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        baseList=response.xpath('//article/a/text()')
        item=DaomuItem()
        i=0
        for base in baseList:
            info=base.extract().split( )
            item['title']=info[0]
            item['chapter']=info[1]
            item['chapterName']=info[2]
            item['link']=response.xpath('//article/a/@href').extract()[i]
            i+=1
            yield item
