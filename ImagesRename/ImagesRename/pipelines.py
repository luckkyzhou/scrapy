# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class ImagesrenamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['imgurl']:
            yield Request(image_url,meta={'name':item['imgname']})

    def file_path(self, request, response=None, info=None): #重命名
        image_guild = request.url.split('/')[-1]
        name = request.meta['name'] #接收上面meta传递过来的图片名称
        name = re.sub(r'[？\\*|“<>:/]', '', name) #过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        filename = u'{0}/{1}'.format(name, image_guild)
        return filename
