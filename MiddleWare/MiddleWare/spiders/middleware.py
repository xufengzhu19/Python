# -*- coding: utf-8 -*-

import scrapy


class MiddlewareSpider(scrapy.Spider):
    name = "middleware"
    allowed_domains = ["www.baidu.com"]
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('执行middleware')

