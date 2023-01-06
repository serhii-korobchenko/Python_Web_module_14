import scrapy


class AuthorsDetailSpider(scrapy.Spider):
    name = 'authors_detail'

    # start custom settings
    custom_settings = {'ITEM_PIPELINES': {
        'serhii_spyder_bot.pipelines.SerhiiSpyderBotPipelineDetail': 400
    },

        "FEEDS": {
            'detail_info.json': {
                'format': 'jsonlines',
                'encoding': 'utf8',
                'overwrite': True,

            },
        },
        "SPIDER_MIDDLEWARES": {
            'serhii_spyder_bot.middlewares.SerhiiSpyderBotSpiderDetailMiddleware': 543,
        }

    }
    # stop custom setting

    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            # yield {
            #     "author": quote.xpath("span/small/text()").extract()
            # }
            about_link = quote.xpath("span/a/@href").get()
            if about_link:
                yield scrapy.Request(url=self.start_urls[0] + about_link, callback=self.parse_detail)

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_detail(self, response):

        yield {
            "author": response.xpath("/html//div[@class='container']//h3[@class='author-title']/text()").extract(),
            "birthday": response.xpath("/html//div[@class='container']//span[@class='author-born-date']/text()").extract(),
            "bornlocation": response.xpath("/html//div[@class='container']//span[@class='author-born-location']/text()").extract()
        }