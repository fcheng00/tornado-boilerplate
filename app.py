#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns

from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

class TornadoBoilerplate(tornado.web.Application):
    def __init__(self, g_dict):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        self._g_dict = g_dict

def main():
    g_dict = dict()
    g_dict["log"] = 'g_logger'
    
    MONGO_DB_URL = 'mongodb://localhost:27017/'
    MONGO_DB_NAME = 'raw_msg_db'
    
    mg_client = MongoClient(MONGO_DB_URL)
    mg_db = mg_client[MONGO_DB_NAME]
    
    g_dict["mongo_client"] = mg_db

    app = TornadoBoilerplate(g_dict)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
