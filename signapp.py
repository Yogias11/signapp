#!/usr/bin/env python
"""
signapp.py 
created by Rolly Maulana Awangga

"""



class Signapp(object):
	def __init__(self):
		self.npm=0

	def getdata(self,NPM): 
		self.data=NPM
		return self.data
	
	def getlastmeet(self,NPM):
		self.last=NPM
		return self.data

