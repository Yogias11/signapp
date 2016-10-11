#!/usr/bin/env python

from cgi import escape
import signapp

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	uri = escape(uri)
	sign = signapp.Signapp()	

	respon="ok"


	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [respon]

