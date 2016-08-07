#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'lambdaTest.py'
__autor__ ='myth'

fields = ['a1','a2','a3']
escaped_fields = ', '.join(map(lambda f: '‘%s’' %f,fields))
print(escaped_fields)