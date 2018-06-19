import scrapy


class QuotesSpider(scrapy.Spider):
    name = "articles"
    start_urls = [
        'https://alistapart.com/articles/',
        ]

    for i in range (1,105):
        start_urls.append('https://alistapart.com/articles/P' + str(i*10) +'/')
        

    def parse(self, response):
        for article in response.css('ul.entry-list'):
            link = article.css('h3.entry-title a::attr(href)').extract()[0]
            link = 'https://alistapart.com'+link
            yield scrapy.Request(url = link, callback =self.parse2)


    def parse2(self, response):
        for line in response.css('div.main-wrapper'):
            yield {
                'title':line.css('h1.entry-title::text').extract(),
                'headings': line.css('h2::text').extract(),
                'sub headings': line.css('h3::text').extract(),
                'text': line.css('p ::text').extract(),


}
