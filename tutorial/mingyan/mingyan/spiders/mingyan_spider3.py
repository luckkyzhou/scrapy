# -*- coding:utf-8 -*-
# css提取多组数据

import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class mingyan(scrapy.Spider):

    name = 'mingyan3'

    start_urls = [
        'http://lab.scrapyd.cn',
    ]

    def parse(self, response):
        targets = response.css('div.quote')
        for target in targets:
            text = target.css('.text::text').extract_first()
            author = target.css('.author::text').extract_first()
            tags = target.css('.tags .tag::text').extract()
            tag = '，'.join(tags)

            filename = '%s-语录.txt' % author
            with open(filename,'wb') as f:
                f.write(text + '\n')
                f.write('标签：' + tag)

        self.log('保存文件：%s' % filename)  # 日志