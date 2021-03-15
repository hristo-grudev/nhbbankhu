import scrapy

from scrapy.loader import ItemLoader

from ..items import NhbbankhuItem
from itemloaders.processors import TakeFirst


class NhbbankhuSpider(scrapy.Spider):
	name = 'nhbbankhu'
	start_urls = ['https://www.nhbbank.hu/bankunkrol/sajtokozlemenyek']

	def parse(self, response):
		post_links = response.xpath('//a[@class="button fright"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="left_side"]/div[@class="text"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=NhbbankhuItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
