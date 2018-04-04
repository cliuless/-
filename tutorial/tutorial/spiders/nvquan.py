import scrapy


class nvquan(scrapy.Spider):
    handle_httpstatus_list = [404]
    name = 'nvquan'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }

    start_urls = [
    "http://chuansong.me/n/2194300143029"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
