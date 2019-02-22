# -*- coding:utf-8 -*-
# css提取多分页

import sys
import scrapy

reload(sys)
sys.setdefaultencoding('utf-8')

class mingyan(scrapy.Spider):

    name = 'mingyan4'

    start_urls = [
        'http://lab.scrapyd.cn'
    ]

    def parse(self, response):
        targets = response.css('div.quote')
        for target in targets:
            text = target.css('.text::text').extract_first()
            author = target.css('.author::text').extract_first()
            tags = target.css('.tags .tag::text').extract()
            tag = '，'.join(tags)
            '''
            <div class="quote post">
	            <span class="text">下面每一幅都是上亿？你造几？</span>
	            <span>作者：<small class="author">天价世界名画</small>
	            <a href="http://lab.scrapyd.cn/archives/55.html">【详情】</a>
	            </span>
	            <p></p>
	            <div class="tags">
	           	标签： <a class='tag' href=http://lab.scrapyd.cn/tag/%E8%89%BA%E6%9C%AF/>艺术</a>，<a class='tag' href=http://lab.scrapyd.cn/tag/%E5%90%8D%E7%94%BB/>名画</a>	        </div>
    	    </div>
            '''

            filename = '语录.txt'
            with open(filename, 'a+') as f:
                f.write(author + '：' + text + '\n')
                f.write('标签：' + tag)
                f.write('\n-------\n')

        next_page = response.css('li.next a::attr(href)').extract_first()
        '''
        <li class="next">
        <a href="http://lab.scrapyd.cn/page/2/">下一页 »</a>
        </li>
        '''
        if next_page is not None:
            next_page = response.urljoin(next_page)
            # urljoin能替我们转换为绝对路径，也就是加上我们的域名，最终next_page为：http://lab.scrapyd.cn/page/2/
            yield scrapy.Request(next_page,callback=self.parse)

        self.log('保存文件：%s' % filename)  # 日志