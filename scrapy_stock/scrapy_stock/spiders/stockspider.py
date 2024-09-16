import scrapy


class StockspiderSpider(scrapy.Spider):
    name = "stockspider"
    allowed_domains = ["www.nseindia.com"]
    start_urls = ["https://www.nseindia.com"]

    def start_requests(self):
        url = 'https://www.nseindia.com'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        
        ScrapedDate=response.css()

        pass
