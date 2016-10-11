#!/usr/bin/env python

from cgi import escape
import signapp

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	cpdt = escape(uri)[1:]

	sign = signapp.Signapp()
	if len(cpdt)%2==0:
		data = sign.decodeData(cpdt)
		respon=''	
		for a in sign.getAllSign(data):
			respon=respon+str(a)
	else:
		respon = "OK"

	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [respon]

