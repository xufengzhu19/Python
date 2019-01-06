# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from Daomu.settings import *


class DaomuPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    print("======")
    def __init__(self):
        self.conn=pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
        self.db=self.conn[MONGODB_DB]
        self.set=self.db[MONGODB_SET]

    def process_item(self,item,spider):
        d=dict(item)
        self.set.insert_one(d)
        return item