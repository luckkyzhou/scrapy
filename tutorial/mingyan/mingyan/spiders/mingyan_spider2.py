# -*- coding:utf-8 -*-
# css选择器提取一组数据

import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class mingyan(scrapy.Spider):

    name = 'mingyan2'

    start_urls=[
        'http://lab.scrapyd.cn',
    ]

    def parse(self, response):
        target = response.css('div.quote')[0]
        text = target.css('.text::text').extract_first() #这里加.是指class选择器，而如果是id选择器，前面应该加#，属于html的知识
        author = target.css('.author::text').extract_first()
        tags = target.css('.tags .tag::text').extract()
        tag = '，'.join(tags) #list转str，list每个元素之间加入逗号

        filename = '%s-语录.txt' % author
        with open(filename,'wb') as f:
            f.write(text + '\n')
            f.write('标签：' + tag)
        self.log('保存文件：%s' % filename) #日志