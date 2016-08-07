#!usr/bin/env python3
# -*- coding：utf-8 -*-
'web server gateway interface Handle' #doc comment
__autor__ = 'myth'

def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]