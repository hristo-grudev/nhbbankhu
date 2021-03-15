import scrapy


class NhbbankhuItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
