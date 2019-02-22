# -*- coding:utf-8 -*-
import scrapy

class mingyan(scrapy.Spider): # 使类mingyan继承scrapy.Spider类

    name = 'mingyan0' # 定义蜘蛛名

    '''def start_requests(self): # 函数通过下面的链接爬取页面
        # 定义要爬取的链接
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse) # 爬取到的页面提交给parse方法处理
            # yield方法可以将循环单独迭代，节省内存并且增强数据的复用性'''
    start_urls = [
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    def parse(self, response):
        page = response.url.split('/')[-2] # 根据链接提取分页。如：/page/1/，提取到1
        filename = 'mingyan-%s.html' % page # 拼接文件名。如：第爬虫实验室 - SCRAPY中文网提供一页的最终文件名是：mingyan-1.html
        with open(filename,'wb') as f: # with open() as f 代替了try方法。try方法的本质是防止报错使得正在进行的操作无法关闭占用内存。
            f.write(response.body) # response.body是刚才下载的页面
        self.log('保存文件：%s' % filename) #日志