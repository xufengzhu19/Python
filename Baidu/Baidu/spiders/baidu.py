# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名
    name = "baidu"
    # 允许爬取的域名
    allowed_domains = ["www.baidu.com"]
    # 起始url
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        with open("Baidu.html","w",encoding="utf-8") as f:
            f.write(response.text)
