# -*- coding: utf-8 -*-
import scrapy

from Csdn.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["blog.csdn.net"]
    # 修改为自己的url，start_urls必须为列表
    start_urls = ['https://blog.csdn.net/sdr_zd/article/details/85558447/']

    # 写自己的逻辑，给item赋值，传给pipelines
    def parse(self, response):
        item=CsdnItem()
        # xpath得到的是列表,extract()获取选择器对象的文本内容
        item['title']=response.xpath('	//h1[@class="title-article"]/text()').extract()[0]
        item['time']=response.xpath('//span[@class="time"]/text()').extract()[0]
        item['number']=response.xpath('//span[@class="read-count"]/text()').extract()[0]

        yield item

