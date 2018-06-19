import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.survey.gov.lk/',
    ]

    def parse(self, response):
        yield {
            'body': response.css('p.m_bottom_23').extract(),
        }