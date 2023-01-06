# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html


from scrapy import signals
from scrapy.http import Response

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class SerhiiSpyderBotSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, or item objects.

        #Response
        # for i in result:
        #     print(f'-----Result: {i}, Type: {type(i)}')
        #     yield i
        # print(f'-----Response: {response.text}, Type: {type(response.text)}')
        # print(f'-----Spider: {spider}, Type: {type(spider)}')
        try:
            for i in result:

                #print(f'-----------------TYPE______{type(i)}')

                if type(i) is dict:
                    for key, value in i.items():
                        #print(f'-----------------LIST______{value}')

                        for item in value:

                            # normalization
                            strip_item = item.strip()
                            first_replace_item = strip_item.replace('”', '')
                            second_replace_item = first_replace_item.replace('“', '')

                            value.insert(0, second_replace_item)
                            value.remove(item)

                            #print(f'-----------------ITEM______{item}')

                yield i
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")


    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SerhiiSpyderBotSpiderDetailMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, or item objects.

        #Response
        # for i in result:
        #     print(f'-----Result: {i}, Type: {type(i)}')
        #     yield i
        # print(f'-----Response: {response.text}, Type: {type(response.text)}')
        # print(f'-----Spider: {spider}, Type: {type(spider)}')
        try:
            for i in result:

                #print(f'-----------------TYPE______{type(i)}')

                if type(i) is dict:
                    for key, value in i.items():
                        #print(f'-----------------LIST______{value}')

                        for item in value:

                            # normalization
                            strip_item = item.strip()
                            first_replace_item = strip_item.replace('”', '')
                            second_replace_item = first_replace_item.replace('in ', '')

                            value.insert(0, second_replace_item)
                            value.remove(item)

                            #print(f'-----------------ITEM______{item}')

                yield i
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")


    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SerhiiSpyderBotDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest



        # new_response = response.replace(body=unescaped_body)
        # return new_response
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
