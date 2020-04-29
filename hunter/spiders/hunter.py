from scrapy.spiders import CrawlSpider
from ..items import *


class Hunter(CrawlSpider):
    name = 'hun73r'
    start_urls = ['https://www.sslproxies.org/']

    def parse(self, response):
        start_point = response.css('#list>div>.table-responsive'
                                   '>table>tbody')
        for tr in start_point.css('tr'):
            spiderItem = HunterItem()

            spiderItem['ip'] = tr.css('td:nth-child(1)::text').extract_first()
            spiderItem['port'] = tr.css('td:nth-child(2)::text').extract_first()

            yield spiderItem


