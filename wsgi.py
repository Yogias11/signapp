#!/usr/bin/env python

from cgi import escape
import signapp

def application(environ, start_response):
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	
	uri = environ['REQUEST_URI']
	request_body = environ['wsgi.input'].read(request_body_size)

	cpdt = escape(uri)[1:]

	sign = signapp.Signapp()

	hbegin = sign.getHtmlBegin()
	if len(cpdt)%2==0:
		data = sign.decodeData(cpdt)
		result =''	
		for a in sign.getAllSign(data):
			result=result+str(a)
	if request_body_size != 0:
		result = request_body
	else:
		result = "OK"
	hend = sign.getHtmlEnd()

	respon = hbegin + result + hend
	start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(response_body)))])
	
	return [respon]

