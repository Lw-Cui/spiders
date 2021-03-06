# -*- coding: utf-8 -*- 

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
import codecs

class TopLabel(CrawlSpider):
	name = "topDirector"
	allowed_domains = ["movie.douban.com"]
	start_urls = [
		"http://movie.douban.com/top250?start=0&filter=&type=",
		#"http://movie.douban.com/subject/1309101/?from=subject-page",
		]
	rules = ( 
		Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250?.*', ), ), follow=True), 
		Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+/$', )), callback='parse_label', follow=True), 
		Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/.*/?from=subject-page$', )), callback='parse_label'), 
	) 
	def parse_label(self, response):
		path = response.css('#info > span:nth-child(1) > span.attrs > a::text')
		with codecs.open('topDirector.txt', 'a', 'utf-8') as file:
			file.write('\n' + path.extract()[0])
			file.close()