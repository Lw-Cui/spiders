# 自然语言处理的基础设施
```
摘要
本文主要通过展示`网络爬虫(Web Crawler)`技术获取信息的过程，以及使用`图云(Word Cloud)`来可视化数据对`自然语言处理(Natural Language Processing)`的巨大作用及其需要改进的地方。
```
## 网络爬虫
####原理

首先我们给爬虫一个初始 url 。这个页面就是爬虫第一个下载的页面，我们接下来的操作也是通过这个页面向四周扩散的。接下来通过这个页面上的链接与我制定的规则进行匹配，如果成功则将这个 url 加入队列，以备下一步的爬取。

我们的爬虫主要做数据采集的工作，因此我们直接从下载后的页面中提取需要的元素并将其储存在文件或者数据库中以备分析。

####使用

为编写网络爬虫而出现的框架有很多，比较有名的有[scrapy](https://github.com/scrapy/scrapy)。本文所讲的爬虫是基于此的。

`Scrapy`是一个非常强大而方便的`python`爬虫框架，我们只需要做少许代码编写即可使用。安装好后，我们可以写出以下[示例片段](https://github.com/scrapy/dirbot)：
```
from scrapy.spider import Spider

#继承 scrapy 库的基类爬虫
class DmozSpider(Spider):
    name = "dmoz" #该爬虫名字
    allowed_domains = ["dmoz.org"] #限定爬虫的爬取范围
	#初始 url
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

	#解析函数，response 即为网页对爬虫 request 的响应   
	def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc
```
之后运行该爬虫即可抓取`Domz.org`的[python 资源](http://www.dmoz.org/Computers/Programming/Languages/Python/Books/)并显示出来。我们也可以对其进行进一步的分析和储存。

更多相关知识请参阅[官方文档](http://doc.scrapy.org/en/latest/index.html)

####爬取成果
爬取了[豆瓣电影](http://movie.douban.com/)高分电影的标签：
```
意大利
经典
成长
天堂电影院
托纳多雷
剧情
意大利电影
……
```
以及高分导演的名单：
```
彼得·威尔
弗朗西斯·福特·科波拉
加布里尔·穆奇诺
大卫·芬奇
莱塞·霍尔斯道姆
宫崎骏
……
```
原因将在后面论述。

####遇到的问题及相应解决
1. 爬虫会被网站的反爬机制拦截
	* 根据`cookie`拦截：禁用`cookie`
	* 根据`IP`拦截：维护`IP pool`来即时更换代理`IP`
	* 根据`request header`拦截：维护`UserAgent Pool`来更换`user agent`

2. 爬取速度过慢
	* 使用[Crawlera](http://scrapinghub.com/crawlera/)来辅助爬虫切换代理

##词云
####介绍
词云是我们强有力的可视化数据的方法，可以非常清晰直观地传播与表达。但问题也是较为明显：提取的高频词如形容词动词等往往不能够表达完整的意思。因此”标签“很程度上决定了词云的质量。这也是为什么我首先抓取了电影标签的原因。

####使用
目前网络上有许多词云在线生成器，自己编写词云也并不是很难的事情。我们可以通过更深的定制来满足自己的需求。本文的词云稍后会给出链接。

####成果

这是根据豆瓣 `Top250`及其他一些高分电影的标签来制作的图云。从中我们可以比较容易的看出优秀的电影作品表现的主要主题。

![](./TopLabel.png) 

同样的，这张电影导演的词云反映了优秀作品比较多的导演。

![](./topDirector.png) 


####需要改进的地方

下一步就要根据`自然语言处理`的成果来优化词云，如根据词性来为词语分配权重等措施来提升词云质量。

##总结与展望
我们可以发现将网页爬虫、自然语言处理和数据可视化结合起来会产生巨大的力量：爬虫可以获取大量而普适的数据方便进行研究和分析；自然语言的处理可以让我们更精确更细致地解读数据；而可视化的各种方法让我们以最小的代价来传播成果推广结论。三者结合在一起可以做更多意想不到的好玩的事情。

##本文用到的部分程序
* 爬虫代码 [spiders](https://github.com/Lw-Cui/spiders)
* 中文自然语言处理库 [snownlp](https://github.com/isnowfy/snownlp)
* 词云制作 [Chinese_cloud](https://github.com/Lw-Cui/Chinese_cloud)