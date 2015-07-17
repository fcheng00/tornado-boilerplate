from handlers.base import BaseHandler
from datetime import date
import json
import logging
logger = logging.getLogger('boilerplate.' + __name__)

from tornado.escape import json_encode
class DirectionHandler(BaseHandler):
    
    
    def get(self):
        #self.render("base.html")
        response = { 'version': '3.5.1',
                     'last_build':  "2015-06-04" }
        
        self.write(response)

    def post(self):
        data = json.loads(self.request.body.decode('utf-8'))
        print('Got JSON data:', data)
        self.write({ 'got' : 'your data' })    
    
    def options(self):
        self.write("win")
        
#===============================================================================
#     def options(self):
#         
#         self.set_header("Access-Control-Allow-Origin", "*")
#         self.set_header("Allow", "HEAD,GET,PUT,POST,DELETE,OPTIONS")
# 
#         self.set_header("Access-Control-Allow-Headers", "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept")
#         self.write(200)
#===============================================================================