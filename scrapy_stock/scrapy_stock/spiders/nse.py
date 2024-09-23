import scrapy
from scrapy_stock.items import ScrapyStockItem
import datetime

class NseSpider(scrapy.Spider):
    name = "nse"
    allowed_domains = ["www.nseindia.com"]
    start_urls = ["https://www.nseindia.com"]

    def requests():
        pass

    
    def parse(self, response):
        date=response.css('span.nifty50-tradedate')
        scrapeddate=date.css('.nifty50-tradedate::text').get()
        scrapeddate=scrapeddate.split(' ')[0]
        scrapeddateitem=ScrapyStockItem()
        todaydate=datetime.datetime.today().strftime('%d-%b-%Y')
        #randomdate=datetime.datetime(2024, 9, 17)
        print (f"today is __{todaydate}__")
        scrapeddateitem['ScrapedDate'] = scrapeddate
        if todaydate == scrapeddate:
            Marketopen = True
        else:
            Marketopen = False
        print (f"today is Marketopen __{Marketopen}__")
        yield scrapeddateitem