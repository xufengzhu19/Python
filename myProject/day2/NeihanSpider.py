import urllib.request
import re


class NeihanSpider():
    def __init__(self):
        self.baseurl = "https://www.neihan8.com/njjzw/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
        self.page = 2

    def getPage(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<div class="text-.*?title="(.*?)">.*?class="desc">(.*?)</div>', re.S)
        rList = p.findall(html)
        self.writePage(rList)

    def writePage(self, rList):
        for rTuple in rList:
            with open("内涵.txt", "a",encoding="utf-8") as f:
                f.write(rTuple[0].strip() + "\n")
                f.write(rTuple[1].strip() + "\n\n")

    def workOn(self):
        self.getPage(self.baseurl)
        while True:
            c = input("成功，是否继续（y/n）:")
            if c.strip().lower() == "y":
                url = self.baseurl + "index_" + str(self.page) + ".html"
                self.getPage(url)
                self.page += 1
            else:
                print("爬取结束")
                break


if __name__ == '__main__':
    spider = NeihanSpider()
    spider.workOn()

