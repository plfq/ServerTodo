#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import web

urls = (
    '/', 'Hello' 
)


class Hello:        
    def GET(self):
        return 'Ma'

app = web.application(urls, globals()).wsgifunc()

if __name__ == "__main__":
    app.run()
    
import os
if 'SERVER_SOFTWARE' in os.environ:
    print "This is BAE environ"
else:
    print "This is local environ"