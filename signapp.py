#!/usr/bin/env python
"""
signapp.py 
created by Rolly Maulana Awangga

"""
import config
import pymongo

class Signapp(object):
	def __init__(self):
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

