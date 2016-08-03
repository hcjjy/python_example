#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'sql Object Relational Mapping'# doc comment
__autor__ = 'myth'

	
class Base(object):
	def __init__(self,id,name):
		self.id = id;
		self.name = name

class User(Base):
	id ='1'
	name = 'huihui'
	
user = Base(id = 2,name = 'xiaohuihui')
print(user.id,user.name)
print(User.id,User.name)