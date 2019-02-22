# -*- coding:utf-8 -*-

import scrapy
import sys
from ImageSpider.items import ImagespiderItem #接入item.py

reload(sys)
sys.setdefaultencoding('utf-8')

class ImagespiderSpider(scrapy.Spider): #继承类
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImagespiderItem() #对象实例化item
        imgurls = response.css('.post-content img::attr(src)').extract()

        item['imgurl'] = imgurls
        yield item
