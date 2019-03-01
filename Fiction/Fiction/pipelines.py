# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class FictionPipeline(object):
    def process_item(self, item, spider):
        curPath = './download'
        tempPath = item['name'] #.decode('unicode_escape')
        targetPath = curPath + os.path.sep + tempPath + '.txt'

        with open(targetPath, 'a') as f:
            f.write(item['chapter_name'] + '\n' + item['chapter_content'] + '\n')
        return item
