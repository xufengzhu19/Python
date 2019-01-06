from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl tengxun -o Tencent.csv'.split())
    # cmdline.execute('scrapy crawl tengxun -o Tencent.json'.split())
