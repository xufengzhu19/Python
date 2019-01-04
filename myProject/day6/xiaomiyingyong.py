# xpath //ul[@id="all-applist"]//li
# 应用名称 ./h5/a
# 应用链接 ./h5/a

import requests
from multiprocessing import Queue
from threading import Thread

import time
from lxml import etree


class XiaoMiSpider:
    def __init__(self):
        self.baseurl = 'http://app.mi.com/category/12?#page='
        self.mainurl = 'http://app.mi.com/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
        # url队列
        self.urlQueue = Queue()
        self.parseQueue = Queue()
        # 解析队列

    # url放入队列
    def getUrl(self):
        for page in range(20):
            url = self.baseurl + str(page)
            self.urlQueue.put(url)

    # 采集线程函数，geturl，将html解析
    def getHtml(self):
        while not self.urlQueue.empty():
            url = self.urlQueue.get()
            res = requests.get(url, headers=self.headers)
            res.encoding = "utf-8"
            html = res.text
            self.parseQueue.put(html)

    # 解析线程函数，gethtml，提取并处理数据
    def getData(self):
        while not self.parseQueue.empty():
            html = self.parseQueue.get()
            parseHtml = etree.HTML(html)
            baseList = parseHtml.xpath('//ul[@id="all-applist"]//li')
            for base in baseList:
                name = base.xpath('./h5/a/text()')[0]
                link = self.mainurl + base.xpath('./h5/a/@href')[0]
                d = {"分类": "学习教育", "名称": name, "链接": link}
                with open('xiaomi.json', 'a', encoding='utf-8') as f:
                    f.write(str(d) + '\n')

    def workOn(self):
        self.getUrl()
        t1List = []
        t2List = []
        for i in range(5):
            t = Thread(target=self.getHtml())
            t1List.append(t)
            t.start()
        for i in t1List:
            i.join()
        for i in range(5):
            t = Thread(target=self.getData())
            t2List.append(t)
            t.start()
        for i in t2List:
            i.join()


if __name__ == '__main__':
    start = time.time()
    spider = XiaoMiSpider()
    spider.workOn()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
