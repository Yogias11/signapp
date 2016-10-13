#!/usr/bin/env python

from cgi import parse_qs
import signapp

def application(environ, start_response):
	## passing environ uwsgi PARAM
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	uri = environ['REQUEST_URI']
	request_body = environ['wsgi.input'].read(request_body_size)
	post = parse_qs(request_body)
	## Declare apps
	sign = signapp.Signapp()
	## Menu Logic
	if sign.getMenu(uri[:4])==1:
		data = sign.decodeData(uri[4:])
		result = ''
		for a in sign.getAllSign(data):
			result=result+str(a)
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		respon = hbegin + result + hend
	if sign.getMenu(uri[:4])==2:
		result1 = request_body
		result2 = post.get('token', [''])[0]
		respon = result1+"<br>"+result2
	else:
		result = "ganteng"
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		respon = hbegin + result + hend
	## Passing HTML to client
	start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(respon)))])
	return [respon]

