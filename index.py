#!/usr/bin/env python
#-*- coding: utf-8 -*-
import web
import os
from setting import urls

if 'SERVER_SOFTWARE' in os.environ:
#    Run in BAE
    app = web.application(urls, globals()).wsgifunc()
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(app)
else:
#    Run in Localhost
    app = web.application(urls, globals())
    if __name__ == "__main__":
        app.run()
class index:
    name = "hello"
    def GET(self):
        return self.name


