from scrapy import cmdline
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import time
import os
import sys
import requests

if __name__ == '__main__':
    while True:
        time.strftime("%H:%M:%S")
        os.system('scrapy crawl wayspider')
        time.sleep(3)

