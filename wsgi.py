#!/usr/bin/env python

from cgi import escape
import signapp

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	cpdt = escape(uri)[1:]

	sign = signapp.Signapp()

	hbegin = sign.getHtmlBegin()
	if len(cpdt)%2==0:
		data = sign.decodeData(cpdt)
		result =''	
		for a in sign.getAllSign(data):
			result=result+str(a)
	else:
		result = "OK"
	hend = sign.getHtmlEnd()

	respon = hbegin + result + hend
	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [respon]

