from scrapy import cmdline
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import time
import os

# def main():
#     setting = get_project_settings()
#     process = CrawlerProcess(setting)
#     didntWorkSpider = ['ceair','jizhou']
#
#     for spider_name in process.spiders.list():
#         if spider_name not in didntWorkSpider:
#             continue
#         print("Running spider %s" % (spider_name))
#         process.crawl(spider_name)
#     process.start()

if __name__ == '__main__':
    while True:
        print(time.strftime("%H:%M:%S"))
        # os.system("scrapy crawl ceair")
        os.system("scrapy crawl jizhou")
        # os.system("scrapy crawl xiamenair")
        time.sleep(1)
    # cmdline.execute('scrapy crawl dahan'.split())
    # cmdline.execute('scrapy crawl jizhou'.split())