# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ImagespiderPipeline(ImagesPipeline):
    '''def process_item(self, item, spider):

        return item
    '''
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            yield Request(image_url)