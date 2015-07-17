'''
Created on Jun 27, 2015

@author: feng
'''

import json

from handlers.base import BaseHandler



import logging
from django.core.checks import messages
logger = logging.getLogger('boilerplate.' + __name__)



class AvcRawMsgHandler(BaseHandler):
    '''
    receive post transaction msgs
    '''           
    def get(self):
        pass
        
    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        print('Got JSON data:', data)
        
        if "mongo_client" in self.application._g_dict:
            mg_client = self.application._g_dict["mongo_client"]
            mg_client.avc_msgs.insert(data)
        else:
            print "something wrong with the database, cannot save msg into db"
                
        if "avcws" in self.application._g_dict:
            for client in self.application._g_dict:
                client.write_message(data)
            
        self.set_status(200)

        