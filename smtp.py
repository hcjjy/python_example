#!/usr/bin/env python
# -*- coding:utf-8 -*-
'email smpt send'#doc comment
__autor__ = 'myth'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))


#输入Email地址和口令：
from_addr = input('From:')
password = input('Password:')
#输入收件人地址:
to_addr = input('To:')
#输入SMTP服务器地址:
smtp_server = input('SMTP server:')

#msg = MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>' +'</body></html>','html','utf-8')
msg = MIMEMultipart()
msg.attach(MIMEText('send with file...','plain','utf-8'))

with open('./test.png','rb') as f:
	#设置附件的MIME和文件名，这里是png类型：
	mime = MIMEBase('image','png',filename='test.png')
	#加上必要的头信息:
	mime.add_header('Content-Disposition','attachment',filename='test.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	#把附件的内容读进来：
	mime.set_payload(f.read())
	#用Base64编码：
	encoders.encode_base64(mime)
	#添加到到MIMEMultipart:
	msg.attach(mime)

msg['From'] = _format_addr('Python爱好者 <%s>' %from_addr)
msg['To'] = _format_addr('管理员<%s>' %to_addr)
msg['Subject'] = Header('can\'t use chinese......','utf-8').encode()

#Text = '<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>' +'</body></html>'
#Subject = Header('来自SMTP的问候......','utf-8').encode()
#msg = ('Subject: ' +Subject) +'\n\n%s' %Text

import smtplib
server = smtplib.SMTP_SSL(smtp_server,465)#SMTP连接默认端口是25,SMTP_SSL连接端口不一定
#server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
