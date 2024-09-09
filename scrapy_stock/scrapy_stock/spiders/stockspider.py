import scrapy


class StockspiderSpider(scrapy.Spider):
    name = "stockspider"
    allowed_domains = ["www.nseindia.com"]
    start_urls = ["https://www.nseindia.com/all-reports"]

    def parse(self, response):
        pass
