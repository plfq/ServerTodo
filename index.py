#-*- coding:utf-8 -*-

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    body=["Hello XiaoMa!\n"]
    return body

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)

import os
if 'SERVER_SOFTWARE' in os.environ:
    print "This is BAE environ"
else:
    print "This is local environ"
