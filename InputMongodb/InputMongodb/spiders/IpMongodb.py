# -*- coding:utf-8 -*-
import scrapy
from InputMongodb.items import InputmongodbItem
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class InputMongodbSpider(scrapy.Spider):
    name = 'InputMongodb'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        item = InputmongodbItem() #实例话item

        targets = response.css('.quote')
        for target in targets:
            item['content'] = target.css('.text::text').extract_first()
            tags = target.css('.tags .tag::text').extract()
            item['tag'] = ','.join(tags)
            yield item #提取的数据交给pipeline
            #完成对content和tag的提取

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            #上一句为将路径转换为绝对路径，但next_page已经是绝对路径了
            yield scrapy.Request(next_page,callback=self.parse) #提取的数据交给parse
        #继续爬下一页

