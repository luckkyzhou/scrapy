# -*- coding:utf-8 -*-

import scrapy
import sys
from ImagesRename.items import ImagesrenameItem

reload(sys)
sys.setdefaultencoding('utf-8')

class ImagesrenameSpider(scrapy.Spider):
    name = 'ImgsRename'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = [
        'http://lab.scrapyd.cn/archives/55.html',
        'http://lab.scrapyd.cn/archives/57.html',
    ]

    def parse(self, response):
        item = ImagesrenameItem()
        imgurls = response.css('.post-content img::attr(src)').extract()
        imgnames = response.css('.post-title a::text').extract_first()

        item['imgurl'] = imgurls
        item['imgname'] = imgnames
        yield item