
from scrapy import cmdline
import pymongo
import multiprocessing
from landchina.StoreInMongoDB import MonQueue
# queue = MonQueue('landchina','land')
# print(queue.pop())
# queue.complete(queue.pop())
if __name__ == '__main__':
    cmdline.execute('scrapy crawl landchina'.split())