import bottle
import os

@bottle.route('/')
def index():
    return "Hello World"

bottle.run(server='gevent', port=os.environ.get('PORT', 5000))
