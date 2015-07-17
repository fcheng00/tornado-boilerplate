from handlers.base import BaseHandler
from datetime import date
import logging
logger = logging.getLogger('boilerplate.' + __name__)

from tornado.escape import json_encode
class FooHandler(BaseHandler):
    
    def get(self):
        #self.render("base.html")
        response = { 'version': '3.5.1',
                     'last_build':  "2015-06-04" }
        try:
            callback = self.get_argument('callback')
            if callback is None:
                self.write(response)
            else:
                jsonp = "{jsfunc}({json});".format(jsfunc=callback, json=json_encode(response))
                self.set_header("Content-Type", "application/javascript")
                self.write(jsonp)
        except:
            print 'error to get argument'
            
        
        

