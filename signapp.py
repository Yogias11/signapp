#!/usr/bin/env python
"""
signapp.py 
created by Rolly Maulana Awangga

"""
import config
import pymongo
import urllib
import json
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
	
	def tokenValidation(self,token):
		url = config.tokenurl+token
		response = urllib.urlopen(url)
		data = response.read()
		if (data['aud'] == config.aud) and (data['iss'] == config.iss):
			ret = data['email']
		else:
			ret = ""
		return ret

