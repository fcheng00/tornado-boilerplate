from handlers.foo import FooHandler
from handlers.direction import DirectionHandler
from handlers.transaction import TranHandler, SocketHandler

url_patterns = [
    (r"/tran", TranHandler),
    (r"/foo", FooHandler),
    (r"/ws", SocketHandler),
    (r"/avcws", AvcSocketHandler),
    (r"/direction", DirectionHandler)
]
