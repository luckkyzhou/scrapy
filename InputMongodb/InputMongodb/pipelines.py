# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class InputmongodbPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1',27017) #连接mongodb
        db = client['InputMongodb'] #连接的数据库名
        self.post = db['test'] #数据需要提交到的表名

    def process_item(self, item, spider):
        postItem = dict(item) #将item转化为字典
        self.post.insert(postItem) #向数据库插入一条数据
        return item
