import scrapy


class NseSpider(scrapy.Spider):
    name = "nse"
    allowed_domains = ["www.nseindia.com"]
    start_urls = ["https://www.nseindia.com"]

    def parse(self, response):
        pass
