# -*- coding: utf-8 -*-

import scrapy
import sys
import re
#from Fiction.items import FictionItem

reload(sys)
sys.setdefaultencoding('utf-8')

class NovelSpider(scrapy.Spider):
    name = 'novel'

    allowed_domains = ['quanshuwang.com']
    start_urls = [
        'http://www.quanshuwang.com/book_9055.html'
    ]

    def parse(self, response):
        read_url = response.css('.b-oper a::attr(href)').extract_first() #获取马上阅读按钮的url，进入章节目录
        yield scrapy.Request(read_url, callback=self.parse_chapter) #将read_url丢给parse_chapter处理

    def parse_chapter(self, response):
        chapter_urls = response.css('.clearfix.dirconone a::attr(href)').extract()
        for chapter_url in chapter_urls:
           yield scrapy.Request(chapter_url, callback=self.parse_content)

    def parse_content(self, response):
        #item = FictionItem()

        #item['name']
        name = response.css('.bookInfo em.l::text').extract_first() #小说名
        #item['chapter_name']
        chapter_name = response.css('.bookInfo strong.l::text').extract_first() #小说章节名

        '''
        获取小说内容
        通过正则来过滤不需要的内容，规则是copy的
        '''
        result = response.text
        chapter_content_reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
        chapter_content_3 = re.findall(chapter_content_reg, result, re.S)[0]
        chapter_content_2 = chapter_content_3.replace('    ', '')
        #item['chapter_content']
        chapter_content_1 = chapter_content_2.replace('<br />', '')
        chapter_content = chapter_content_1.replace('&nbsp;', '')

        filename = '%s.txt' % name
        with open(filename, 'a') as f:
            f.write(chapter_name + '\n\n' + chapter_content + '\n\n')