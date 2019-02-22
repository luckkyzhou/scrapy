# -*- coding:utf-8 -*-

import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8') #解决由python字符集带来的存储文件为空的问题

class mingyan(scrapy.Spider):

    name = 'mingyan1'

    start_urls=[
        'http://lab.scrapyd.cn',
    ]

    def parse(self, response):
        filename = 'mingyan.txt'
        target = response.css('title::text').extract_first()
        print 'target: ' + target
        with open(filename,'wb') as f:
            f.write(target)
        self.log('保存文件：%s' % filename) #日志