#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'getattrTest'# doc comment
__autor__ = 'myth'

class ClsA(object):
	def __init__(self,id,name):
		self.id = id
		self.name = name
	def callgetattr(self,id):
		value = getattr(self,id,None)
		return value
		
clsa = ClsA(1,'huihui')
print(clsa.callgetattr('id'))
