# coding=utf-8
import scrapy


class FuZhouItems(scrapy.Item):
    expDeptTime = scrapy.Field()
    expArrTime = scrapy.Field()
    actDeptTime = scrapy.Field()
    actArrTime = scrapy.Field()
    status = scrapy.Field()
    airline = scrapy.Field()
    airlineCorp = scrapy.Field()