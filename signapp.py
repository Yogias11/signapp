#!/usr/bin/env python
"""
signapp.py 
created by Rolly Maulana Awangga

"""
import config
import pymongo
import urllib
from Crypto.Cipher import AES

class Signapp(object):
	def __init__(self):
		self.key = config.key
		self.iv = config.iv
		self.opendb()

	def opendb(self): 
		self.conn = pymongo.MongoClient(config.mongohost, config.mongoport)
		self.db = self.conn.signapp
	
	def getAllSign(self,NPM):
		self.db.sign
		return self.db.sign.find({"NPM":NPM})
	
	def getLastSign(self,NPM):
		self.db.sign
		return self.db.sign.find_one({"NPM":NPM})
	
	def insertSign(self,NPM,Nilai,rcvdate):
		self.db.sign
		data = {"NPM":NPM,"Nilai":Nilai,"waktu":rcvdate}

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

