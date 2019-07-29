# -*- coding: utf-8 -*-
import scrapy
import json
from doubanspider.items import DoubanspiderItem

class Douban2018Spider(scrapy.Spider):
    name = 'douban2018'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/ithil_j/activity/book_annual2018/widget/1']

    def parse(self, response):
        item = DoubanspiderItem()
        # for i in range(1, 37):
        page = json.loads(response.body)
        tag = page['res']['kind_str']

        if tag != 'excerpt':
            sort_name = page['res']['payload']['title']
            subjects = page['res']['subjects']
            item['sort_name'] = sort_name
            # yield item
            for n, book in enumerate(subjects):
                number = n + 1
                title = book['title']
                rating = book['rating']
                item['number'] = number
                item['title'] = title
                item['rating'] = rating
                yield item
        next_page = int(response.url.split('/')[-1]) + 1
        next_url = response.urljoin(str(next_page))
        yield scrapy.Request(next_url, callback=self.parse)



