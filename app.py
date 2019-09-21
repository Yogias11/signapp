from flask import Flask, escape, request
import signapp



app = Flask(__name__)
sign = signapp.Signapp()


@app.route('/')
def hello():
    name = request.args.get("name", "Crot")
    return f'Hello, {escape(name)}!'
    
@app.route('/<name>')
def menu(name):
	url=sign.urlDecode16(name)
	if sign.getMenu(url[:3])=="key":
		data = url[3:]
		result = sign.getPhoto(data)
		a = sign.getAllSign(data)
		result=result+"<li> Nilai rata-rata saat ini: "+str(a)+"</li>"
		result = result+"</ul>"
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		tokenuriparam = sign.tokenUri()
		urlenc = sign.urlEncode16(tokenuriparam)
		sign.setTTL(urlenc)
		hend = hend.replace("TOKENURIPARAM",urlenc)
		form = sign.getHtmlForm()
		form = form.replace("NPMVALUE",data)
		respon = hbegin + result + form + hend
	else:
		result = url
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()
		tokenuriparam = sign.tokenUri()
		hend = hend.replace("TOKENURIPARAM",sign.urlEncode16(tokenuriparam))
		respon = hbegin + result + hend
	return respon
    
@app.route('/<name>', methods=['POST'])
def storedata(name):
	url=sign.urlDecode16(name)
	if sign.getMenu(url[:5])=="token":
		token = request.form['token']
		npm = request.form['NPM']
		numb = request.form['Nilai']
		pemb = request.form['Topik']
		html = sign.getTokenData(token)
		email = sign.getJsonData('email',html)
		if sign.emailAcl(email):
			if sign.getTTL(name):
				respon = sign.insertTodayOnly(npm,numb,email,pemb)
			else:
				respon = "expire"
		else:
			respon = "invalid"
	return respon