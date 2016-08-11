import mod
#from config import *
import config
def fun():
	print(config.x)#x)
fun()
#使用from config import *中的x改变只对本文件有效，而使用import config可以跨文件(模块)