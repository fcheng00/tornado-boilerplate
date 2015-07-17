'''
Created on Jun 27, 2015

@author: feng
'''

from tornado import websocket

class AvcSocketHandler(websocket.WebSocketHandler):
    '''
    classdocs
    '''
    # this is for disabling the 403 forbidden warning
    def check_origin(self, origin):
        return True
    
    def open(self):
        ''' ran once an open ws connection is made'''
        if "avcws" not in self.application._g_dict:
            self.application._g_dict["avcws"] = list()
            self.application._g_dict["avcws"].append(self) 
        else:
            avc_ws_list = self.application._g_dict["avcws"]
            if self not in avc_ws_list:
                avc_ws_list.append(self)
            
        print "print client connected"
            
    def on_message(self, message):
        print message
        self.write_message(u"You said: " + message)

    def on_close(self):
        ''' on close event, triggered once a connection is closed'''
        avc_ws_list = self.application._g_dict["avcws"]
        if self in avc_ws_list:
            avc_ws_list.remove(self)
