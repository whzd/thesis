import scrapy
import os.path

class DefaultSpider(scrapy.Spider):
    name = "default"

    def __init__(self, *args, **kwargs):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, "configs/%s.txt" % self.name)
        with open(abs_file_path) as f:
            self.start_urls = [line.strip() for line in f.readlines()]

    def parse(self, response):
        tmpDir = './raw-files/'
        page = response.url.split("/")[-1].replace(" ", "")
        filename = 'page-%s.html' % page
        file_path = os.path.join(tmpDir, filename)
        if not os.path.isdir(tmpDir):
            os.mkdir(tmpDir)
        with open(file_path, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
