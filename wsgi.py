#!/usr/bin/env python

from cgi import escape
import signapp

def application(environ, start_response):
	## passing environ uwsgi PARAM
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	uri = environ['REQUEST_URI']
	request_body = environ['wsgi.input'].read(request_body_size)
	## Declare apps
	sign = signapp.Signapp()
	## Menu Logic
	if sign.getMenu(uri[:4])==1:
		data = sign.decodeData(uri[4:])
		result = ''
		for a in sign.getAllSign(data):
			result=result+str(a)
	if sign.getMenu(uri[:4])==2:
		result = request_body
	else:
		result = "OK"
	## Passing HTML to client
	hbegin = sign.getHtmlBegin()
	hend = sign.getHtmlEnd()
	respon = hbegin + result + hend
	start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(respon)))])
	return [respon]

