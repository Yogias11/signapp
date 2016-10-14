#!/usr/bin/env python
"""
signapp.py 
created by Rolly Maulana Awangga

"""
import config
import pymongo
import urllib
import random
import time
from Crypto.Cipher import AES

class Signapp(object):
	def __init__(self):
		self.key = config.key
		self.iv = config.iv
		self.opendb()

	def opendb(self): 
		self.conn = pymongo.MongoClient(config.mongohost, config.mongoport)
		self.db = self.conn.signapp
	
	def tokenUri(self):
		return config.tokenuri

	def random(self,ln):
                ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                chars=[]
                for i in range(ln):
                        chars.append(random.choice(ALPHABET))
                return "".join(chars)

	def urlEncode16(self,uri):
		ln = len(uri)
		sp = 16 - ln - len(str(ln))
		if ln>9:
			dt = str(ln)+uri+self.random(sp)
		else:
			dt = "0"+str(ln)+uri+self.random(sp-1)
		return self.encodeData16(dt)

	def urlDecode16(self,uri):
		if len(uri)%16 == 0:
			dt = self.decodeData16(uri)
			try:
				int(dt[:2])
				ln = int(dt[:2])
				ret = dt[2:2+ln]
			except ValueError:
				ret = dt
		else:
			ret = uri
		return ret		

	def getAllSign(self,NPM):
		self.db.sign
		return self.db.sign.find({"NPM":NPM})
	
	def getLastSign(self,NPM):
		self.db.sign
		return self.db.sign.find_one({"NPM":NPM})
	
	def insertSign(self,NPM,Nilai,Pembimbing):
		self.db.sign
		data = {"NPM":NPM,"Nilai":Nilai,"waktu":time.strftime("%d/%m/%Y"),"Pembimbing":Pembimbing}
		idProcess = self.db.sign.insert_one(doc).inserted_id
		return str(idProcess)

	def encodeData(self,msg):
		obj=AES.new(self.key,AES.MODE_CFB,self.iv)
		cp = obj.encrypt(msg)
		return cp.encode("hex")

	def decodeData(self,msg):
		obj=AES.new(self.key,AES.MODE_CFB,self.iv)
		dec = msg.decode("hex")
		return obj.decrypt(dec)

	def encodeData16(self,msg):
		obj=AES.new(self.key,AES.MODE_CBC,self.iv)
		cp = obj.encrypt(msg)
		return cp.encode("hex")

	def decodeData16(self,msg):
		obj=AES.new(self.key,AES.MODE_CBC,self.iv)
		dec = msg.decode("hex")
		return obj.decrypt(dec)

	def getHtmlBegin(self):
		return config.html_begin

	def getHtmlEnd(self):
		return config.html_end

	def getHtmlForm(self):
		return config.html_form

	def getMenu(self,uri):
		if uri == config.keyuri:
			opsi = "key"
		elif uri == config.tokenuri:
			opsi = "token"
		else:
			opsi = "other"
		return opsi
	
	def getTokenData(self,token):
		url = config.tokenurl+token
		response = urllib.urlopen(url)
		html = response.read()
		return html

	def tokenValidation(self,token):
		html = self.getTokenData(token)
		if (html.find(config.aud)>0) and (html.find(config.iss)>0):
			ret = "valid"
		else:
			ret = "invalid"
		return ret

	def getJsonData(self,name,json):
		lookup = '"%s": "'%name
		b = json.find(lookup)
		c = json[b:].find(':')
		c+=1
		b = b+c
		c = json[b:].find(',')
		c = b+c
		data = json[b:c].strip().strip('"')
		return data

