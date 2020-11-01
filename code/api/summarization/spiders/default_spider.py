import scrapy
import os.path

class DefaultSpider(scrapy.Spider):
    name = "default"

    custom_settings = {
            'DEPTH_LIMIT': 1
            }

    def __init__(self, link='', target='', **kwargs):
        url = link + target
        self.start_urls = [url]

    def parse(self, response):
        page = response.url.split("/")[-1].replace(" ", "")
        self.saveFile(page, response.body)
        followUps = response.xpath('/html/body/div[3]/div[3]/div[5]/div[1]//a/@href').extract()
        for next_page in followUps:
            if (next_page is not None) and (next_page.startswith('/wiki')):
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)

    def saveFile(self, pageName, pageContent):
        tmpDir = './raw-files/'
        filename = 'page-%s.html' % pageName
        file_path = os.path.join(tmpDir, filename)
        if not os.path.isdir(tmpDir):
            os.mkdir(tmpDir)
        with open(file_path, 'wb') as f:
            f.write(pageContent)
        self.log('Saved file %s' % filename)


