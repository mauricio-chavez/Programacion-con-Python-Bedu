import scrapy
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):  
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)




body = '<html><body><span>good</span></body></html>'

print(Selector(text=body).xpath('//span/text()').get())
print(Selector(text=body).css('span::text').get())