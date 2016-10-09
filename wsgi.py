#!/usr/bin/env python

from cgi import escape
import config
import gitar

def application(environ, start_response):
	uri = environ['REQUEST_URI']

	uri = escape(uri)
	gr = gitar.Gitar()	

	if uri == config.uri1:
		respon=gr.gitpull(config.dir1,config.host1,config.username1,config.password1)		
		respon=str(respon[0])
	elif uri == config.gmsuri:
		title="<h3>error log GMS server</h3>"
                html=title+"<h4>Server GMS 1 : </h4>"
                respon=gr.getlog(config.logpath,config.gms1,config.username,config.password)
                respon=html+str(respon[0])
                html="<h4>Server GMS 2 : </h4>"
                respont=gr.getlog(config.logpath,config.gms2,config.username,config.password)
                respon=respon+html+str(respont[0])
                html="<h4>Server GMS 4 : </h4>"
                respont=gr.getlog(config.logpath,config.gms4,config.username,config.password)
                respon=respon+html+str(respont[0])
	elif uri == config.portaluri:
                title="<h3>error log portal server</h3>"
                html=title+"<h4>Server portal 1 : </h4>"
                respon=gr.getlog(config.logpath,config.portal1,config.username,config.password)
                respon=html+str(respon[0])
                html="<h4>Server portal 2 : </h4>"
                respont=gr.getlog(config.logpath,config.portal2,config.username,config.password)
                respon=respon+html+str(respont[0])
                html="<h4>Server portal 3 : </h4>"
                respont=gr.getlog(config.logpath,config.portal3,config.username,config.password)
                respon=respon+html+str(respont[0])
		html="<h4>Server portal 4 : </h4>"
                respont=gr.getlog(config.logpath,config.portal4,config.username,config.password)
                respon=respon+html+str(respont[0])
	elif uri == config.gmssuri:
                title="<h3>error log GMSS server</h3>"
                html=title+"<h4>Server GMSS 1 : </h4>"
                respon=gr.getlog(config.logpath,config.gmss1,config.username,config.password)
                respon=html+str(respon[0])
                html="<h4>Server GMSS 2 : </h4>"
                respont=gr.getlog(config.logpath,config.gmss2,config.username,config.password)
                respon=respon+html+str(respont[0])
                html="<h4>Server GMSS 3 : </h4>"
                respont=gr.getlog(config.logpath,config.gmss3,config.username,config.password)
                respon=respon+html+str(respont[0])
	else:
		respon="oke"


	start_response('200 OK', [('Content-Type', 'text/html')])
	
	return [respon]

