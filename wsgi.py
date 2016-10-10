#!/usr/bin/env python

from cgi import escape
import config
import signapp

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	uri = escape(uri)
	sign = signapp.Signapp()	

	if uri == config.uri1:
		respon=uri		
		respon=str(respon[0])
	elif uri == config.gmsuri:
                respont=uri
                respon=str(respont[0])
	else:
		respon="oke"


	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [respon]

