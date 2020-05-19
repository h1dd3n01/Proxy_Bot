import scrapy


class HunterItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
