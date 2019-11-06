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
    url = sign.urlDecode16(name)
    if sign.getMenu(url[:3]) == "key":
        data = url[3:].split('%')[0]
        nilai = url[3:].split('%')[1]
        komentar = url[3:].split('%')[2]
        pertemuanke = url[3:].split('%')[3]
        if int(pertemuanke) == sign.getPertemuan():
            sign.opendb()
            result = sign.getPhoto(data)
            a = sign.getAllSign(data)
            b = sign.getPertemuan()
            result = result + "<li> Nilai rata-rata saat ini: " + str(a) + "</li>"
            result = result + "<li> Saat ini penilaian untuk pertemuan ke : " + str(b) + "</li>"
            result = result + "</ul>"
            hbegin = sign.getHtmlBegin()
            hend = sign.getHtmlEnd()
            tokenuriparam = sign.tokenUri()
            urlenc = sign.urlEncode16(tokenuriparam)
            # sign.setTTL(urlenc)
            hend = hend.replace("TOKENURIPARAM", urlenc)
            form = sign.getHtmlForm()
            form = form.replace("NPMVALUE", data)
            form = form.replace("KOMENTARVALUE", komentar)
            form = form.replace("NILAIVALUE", nilai)
            respon = hbegin + result + form + hend
        else:
            respon = "qrcode pertemuan ke " + pertemuanke
    else:
        result = url
        hbegin = sign.getHtmlBegin()
        hend = sign.getHtmlEnd()
        tokenuriparam = sign.tokenUri()
        hend = hend.replace("TOKENURIPARAM", sign.urlEncode16(tokenuriparam))
        respon = hbegin + result + hend
    return respon


@app.route('/<name>', methods=['POST'])
def storedata(name):
    url = sign.urlDecode16(name)
    if sign.getMenu(url[:5]) == "token":
        token = request.form['token']
        npm = request.form['NPM']
        numb = request.form['Nilai']
        pemb = request.form['Topik']
        html = sign.getTokenData(token)
        email = sign.getJsonData('email', html)
        if sign.emailAcl(email):
            respon = sign.insertTodayOnly(npm, numb, email, pemb)
        else:
            respon = "invalid"
    return respon
