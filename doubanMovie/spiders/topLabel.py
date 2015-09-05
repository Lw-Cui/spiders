# -*- coding: utf-8 -*- 

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import codecs

class TopLabel(CrawlSpider):
	name = "topLabel"
	allowed_domains = ["movie.douban.com"]
	start_urls = [
		"http://movie.douban.com/top250?start=0&filter=&type=",
		]
	rules = ( 
		Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250?.*', ), ), follow=True), 
		Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+/$', )), callback='parse_label', follow=True), 
		Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+/?from=subject-page', )), callback='parse_label', follow=True), 
	) 
	def parse_label(self, response):
		index = 1
		while (True):
			path = response.xpath('//*[@id="content"]/div[2]/div[2]/div[5]/div/a[%d]/text()' % index)
			if not path:
				break
			with codecs.open('TopLabel.txt', 'a', 'utf-8') as file:
				file.write('\n' + path.extract()[0])
				file.close()
			index += 1

	def add_cookie(self, request):
		pass