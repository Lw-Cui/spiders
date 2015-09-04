# -*- coding: utf-8 -*- 

from scrapy.spiders import Spider
import scrapy
import codecs

class TopLabel(Spider):
	name = "top250"
	allow_domains = ['movie.douban.com']
	start_urls = [
		"http://movie.douban.com/top250",
	]

	def parse(self, response):
		self.parse_movie(response)

		href = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/link/@href')
		if href:
			url = response.urljoin(href.extract()[0])
			yield scrapy.Request(url)

	def parse_movie(self, response):
		with codecs.open('Top250.txt', 'a', 'utf-8') as file:
			for i in range(25):
				file.write('\n' + response.xpath('//*[@id="content"]/div/div[1]/ol/li[%d]/div/div[2]/div[1]/a/span[1]/text()' % (i + 1)).extract()[0])
			file.close()