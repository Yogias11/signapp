from flask import Flask, escape, request
import signapp



app = Flask(__name__)
sign = signapp.Signapp()


@app.route('/')
def hello():
    name = request.args.get("name", "Crot")
    return f'Hello, {escape(name)}!'
    
@app.route('/<name>')
def belanja(name):
    url=sign.urlDecode16(name)
	if sign.getMenu(url[:3])=="key":
		data = url[3:]
		result = '<h2>'+data+'</h2><img src="https://cdn.vas.web.id/foto/'+data+'.png"><ol>'
		for a in sign.getAllSign(data):
			result=result+"<li>"+str(a)+"</li>"
		result = result+"</ol>"
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		tokenuriparam = sign.tokenUri()
		urlenc = sign.urlEncode16(tokenuriparam)
		sign.setTTL(urlenc)
		hend = hend.replace("TOKENURIPARAM",urlenc)
		form = sign.getHtmlForm()
		form = form.replace("NPMVALUE",data)
		respon = hbegin + result + form + hend
	elif sign.getMenu(url[:3])=="token":
		token = post.get('token', [''])[0]
		npm = post.get('NPM', [''])[0]
		numb = post.get('Nilai', [''])[0]
		pemb = post.get('Topik', [''])[0]
		html = sign.getTokenData(token)
		email = sign.getJsonData('email',html)
		if sign.emailAcl(email):
			if sign.getTTL(uri[1:]):
				respon = sign.insertTodayOnly(npm,numb,email,pemb)
			else:
				respon = "expire"
		else:
			respon = "invalid"
	else:
		result = url
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		tokenuriparam = sign.tokenUri()
		hend = hend.replace("TOKENURIPARAM",sign.urlEncode16(tokenuriparam))
		respon = hbegin + result + hend
    return respon
    
    