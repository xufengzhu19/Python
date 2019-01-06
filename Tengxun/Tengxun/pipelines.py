# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql

from Tengxun.settings import *


class TengxunPipeline(object):
    def process_item(self, item, spider):
        print("TengxunPipeline")
        return item


class MongoPipeline(object):
    def __init__(self):
        # 创建连接
        self.conn = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        # 库对象
        self.db = self.conn[MONGODB_DB]
        # 集合
        self.myset = self.db[MONGODB_SET]

    def process_item(self, item, spider):
        print("MongoPipeline")
        d = dict(item)
        self.myset.insert_one(d)
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PWD, database=MYSQL_DB,
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        print("MysqlPipeline")
        ins = 'insert into tencentjob values(%s,%s,%s,%s,%s,%s)'
        L = [item['jobName'],
             item['jobCategory'],
             int(item['jobNumber'].strip()),
             item['jobAddress'],
             item['pubTime'],
             item['jobLink']]
        self.cursor.execute(ins, L)
        self.db.commit()
        return item

    # process执行完成后会执行此方法
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print("mysql already close")