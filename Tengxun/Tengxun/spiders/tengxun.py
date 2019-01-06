# -*- coding: utf-8 -*-
import scrapy

from Tengxun.items import TengxunItem


class TengxunSpider(scrapy.Spider):
    name = "tengxun"
    allowed_domains = ["hr.tencent.com"]
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(0)]

    def parse(self, response):
        # 284页url地址给调度器入队列
        for i in range(0, 2831, 10):
            url=self.url + str(i)
            yield scrapy.Request(url, callback=self.parseHtml)

    def parseHtml(self, response):
        item = TengxunItem()
        baseList = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for base in baseList:
            item['jobName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['jobCategory'] = base.xpath('./td[2]/text()').extract()
            if item['jobCategory']:
                item['jobCategory']=item['jobCategory'][0]
            else:
                item['jobCategory']='无'
            item['jobNumber'] = base.xpath('./td[3]/text()').extract()[0]
            item['jobAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['pubTime'] = base.xpath('./td[5]/text()').extract()[0]
            item['jobLink'] = base.xpath('./td[1]/a/text()').extract()[0]

            yield item
