class DefaultSpider(scrapy.Spider):
    name = "default"

    custom_settings = {
            'DEPTH_LIMIT': 1
            }

    def __init__(self, *args, **kwargs):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, "configs/%s.txt" % self.name)
        with open(abs_file_path) as f:
            self.start_urls = [line.strip() for line in f.readlines()]

    def parse(self, response):
        page = response.url.split("/")[-1].replace(" ", "")
        self.saveFile(page, response.body)
        for next_page in response.css('element.mw-body-content > p > a::attr(href)').extract_first():
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
