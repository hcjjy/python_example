#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'Handle HTML' #文档注释
__autor__ = 'myth'
from html.parser import HTMLParser
from html.entities import name2codepoint
import html,io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class MyHTMLParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		print('<%s>' %tag)
		
	def handle_endtag(self,tag):
		print('</%s>' %tag)
		
	def handle_startendtag(self,tag,attrs):
		print('<%s/>' %tag)
		
	def handle_data(self,data):
		data = data.replace(u'\xa0', ' ')
		#data = 
		print(data)
		
	def handle_comment(self,data):
		print('<!--',data,'-->')
		
	def handle_entityref(self, name):
		print('&%s:' %name)
		
	def handle_charref(self,name):
		print('&#%s:' %name)
		
parser = MyHTMLParser()
text = '''<html>
<head></head>
<body>
<!-- test html parser -->
   <p>Some <a href=\"#\">html</a>HTML;&nbsp;tutorial...<br>END</p> 
</body></html>'''

parser.feed(text)
#<p>Some <a href=\"#\">html</a> HTML&#1234;tutorial...<br>END</p>