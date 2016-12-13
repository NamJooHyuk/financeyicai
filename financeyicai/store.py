#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_yicaiDB = client[settings['MONGODB_DB']]
collect_yicai_161212 = News_yicaiDB[settings['MONGODB_COLLECTION']]