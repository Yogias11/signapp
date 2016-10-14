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
	url=sign.urlDecode16(uri[1:])
	if sign.getMenu(url[:3])=="key":
		data = url[3:]
		result = "<ol>"
		for a in sign.getAllSign(data):
			result=result+"<li>"+str(a)+"</li>"
		result = result+"</ol>"
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		tokenuriparam = sign.tokenUri()
		hend = hend.replace("TOKENURIPARAM",sign.urlEncode16(tokenuriparam),1)
		form = sign.getHtmlForm()
		form = form.replace("NPMVALUE",data)
		respon = hbegin + result + form + hend
	elif sign.getMenu(url[:3])=="token":
		token = post.get('token', [''])[0]
		npm = post.get('npm', [''])[0]
		numb = post.get('numb', [''])[0]
		html = sign.getTokenData(token)
		email = sign.getJsonData('email',html)
		respon = sign.insertSign(npm,numb)
	else:
		result = url
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		tokenuriparam = sign.tokenUri()
		hend = hend.replace("TOKENURIPARAM",sign.urlEncode16(tokenuriparam),1)
		respon = hbegin + result + hend
	## Passing HTML to client
	start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(respon)))])
	return [respon]

