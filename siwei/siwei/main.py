
import time
import os
from scrapy import cmdline
def main():
    cmdline.execute('scrapy crawl nitrafficindex'.split())
if __name__ == '__main__':
    while True:
        os.system('scrapy crawl nitrafficindex')
        time.sleep(300)



