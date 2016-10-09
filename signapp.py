#!/usr/bin/env python
"""
gitar.py 
created by Rolly Maulana Awangga

"""

import paramiko


class Gitar(object):
	def __init__(self):
		self.ssh=paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	def gitpull(self,dir,host,user,pwd): 
		self.ssh.connect(host,username=user,password=pwd)
		stdin,stdout,stderr=self.ssh.exec_command("cd "+dir+";git pull")
		return stdout.readlines()
	
	def getlog(self,pathf,host,user,pwd):
		self.ssh.connect(host,username=user,password=pwd)
		stdin,stdout,stderr=self.ssh.exec_command("tail -n1 "+pathf)
		return stdout.readlines()

