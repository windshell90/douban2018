# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sort_name = scrapy.Field()
    number = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
