# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZizhuhouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    projectName = scrapy.Field()
    projectLoc = scrapy.Field()
    areaType = scrapy.Field()
    applyAdress = scrapy.Field()
    builderName = scrapy.Field()
    houseName = scrapy.Field()
    salePrice = scrapy.Field()
    serviceLine = scrapy.Field()

