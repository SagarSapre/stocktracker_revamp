import scrapy


class StockspiderSpider(scrapy.Spider):
    name = "stockspider"
    allowed_domains = ["www.nseindia.com"]
    start_urls = ["c"]

    def start_requests(self):
        url = 'https://www.nseindia.com'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        pass
