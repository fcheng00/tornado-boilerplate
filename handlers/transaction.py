'''
Created on May 16, 2015

@author: feng
'''
from tornado import websocket, web, ioloop
import json

from handlers.base import BaseHandler

import logging
from django.core.checks import messages
logger = logging.getLogger('boilerplate.' + __name__)

cl = []

class SocketHandler(websocket.WebSocketHandler):
    ''' websocket handler '''
    # this is for disabling the 403 forbidden warning
    def check_origin(self, origin):
        return True
    
    def open(self):
        ''' ran once an open ws connection is made'''
        if self not in cl:
            cl.append(self)
            
        print "print client connected"
            
    def on_message(self, message):
        print message
        self.write_message(u"You said: " + message)

    def on_close(self):
        ''' on close event, triggered once a connection is closed'''
        if self in cl:
            cl.remove(self)

class TranHandler(BaseHandler):
    '''
    receive post transaction msgs
    '''       
    
    def get(self):
        print self.application._g_dict
        for item in cl:
            print item
            print "send message to websocket client"
        
    def post(self):
        print self.application.g_dict
        pass
        