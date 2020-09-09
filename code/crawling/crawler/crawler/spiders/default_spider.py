import scrapy
import os.path

class DefaultSpider(scrapy.Spider):
    name = "default"
    start_urls = [
            'https://en.wikipedia.org/wiki/Manga',
            ]

    def parse(self, response):
        directory = '../raw-files/'
        page = response.url.split("/")[-2]
        filename = 'page-%s.html' % page
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(file_path, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
