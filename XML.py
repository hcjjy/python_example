#!usr/bin/env python3
#-*- conding: utf-8 -*-
'SAX simple API for XML' #文档注释
__autor__ = 'myth'

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self,name,attrs):
		print('sax: start_element: %s,attrs: %s' %(name,str(attrs)))
	
	def end_elemnet(self, name):
		print('sax: end_elemnet: %s' % name)
	
	def char_data(self, text):
		if not text:
			print('NULL')
		else:
			print('sax:char_data: %s' %text)
		
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
	<yweather:location city="Beijing" region="" country="China"/>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_elemnet
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)



L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(('some & data'))
L.append(r'</root>')
print(''.join(L))
