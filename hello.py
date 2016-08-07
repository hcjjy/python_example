# -*- coding: utf-8 -*-
#name = input('please enter your name: ')
#print('hello,', name)
 
#print absolure value of an integer
# a = 100
# if a >= 0:
	# print(a)
# else:
	# print(-a)
	

# age = 17
# if age >= 18:
	# print('adult')
# else:
	# print('teenager')
# name = 'heqinghui'
# print(name)

# a = b = 3
# print (u'中文测试正常')

# age = 3
# if age >= 18:
	# print('your age is',age)
	# print('adult')
# elif age >=6:
	# print('your age is',age)
	# print('teenager')
# else:
	# print('kid')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
	# print('00前')
# else:
	# print('00后')
	
# names = ['he','qing','hui']
# for name in names:
	# print(name)
	
# sum = 0
# for x in [1,2,3,4,5,6,7,8,9,10]:
	# sum += x
# print(sum)
	
# sum = 0
# for x in list(range(101)):
	# sum = sum + x
# print(sum)
	
# sum = 0
# n = 99
# while n > 0:
	# sum = sum + n
	# n = n - 2
# print(sum)
# def my_abs1(x):
	# if x>= 0:
		# return x
	# else:
		# return -x
# print(my_abs1(-12))
	
# import math

# def move(x,y,step,angle=0):
	# nx = x + step * math.cos(angle)
	# ny = y - step * math.sin(angle)
	# return nx,ny

# def power(x, n=2):
    # s = 1
    # while n > 0:
        # n = n - 1
        # s = s * x
    # return s
# def enroll(name, gender,age=6, city='Beijing'):
	# print('name:', name)
	# print('gender:', gender)
	# print('city:', city)
# enroll('sarah','F',city = 'nanchang')

# def add_end1(L = None):
	# if L is None:
		# L = []
	# L.append('END')
	# return L
# def calc(*numbers):
	# sum = 0
	# for n in numbers:
		# sum = sum + n*n;
	# return sum

# print(calc(*(2,2,3)))
# print(calc(*[1,3,5,7]))
# print(calc(1,2,3))
# print(calc())

# def person(name,age,**kv):
	# print(name,age,kv)

# person('heqinghui',12,city = 'Beijing')	
# person('xiao',14,**{'city' : 'nanchang','job' : 'Engineer'})

# def person(name, age, *argc,city, job):
	# print(name,age,argc,city,job)
# person('jack',12,*('he',3),city = 'nanchang',job = 'enginer')
	
# def f1(a,b,c = 0,*args,**kw):
	# print(a,b,c,args,kw)
# def f2(a,b,c = 0,* ,d,**kw):
	# print(a,b,c,d,kw)
# print(f1(1,2))
# print(f1(1,2,3))
# print(f1(1,2,3,'a','b'))
# print(f1(1,2,3,'a','b',x = 99))
# print(f2(1,2,d= 99, ext = None))

# args = (1,2,3,4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
# args = {1,2,3}
# kw = {'d': 77,'x': '#'}
# f2(*args,**kw)

# def fact(n):
	# if n==1:
		# return 1
	# return n* fact(n -1)

# print(fact(1))
# print(fact(1000))

def fact(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num-1,num*product)

print(fact(5))

def he (n):
	if n == None:
		pass
he(1)
# L=[]
# n = 1
# while n<= 99:
	# L.append(n)
	# n = n + 2

# def fib(max):
	# n,a,b = 0,0,1
	# while n < max:
		# yield(b)
		# a,b = b, a + b
		# n = n + 1
	# return 'done'

# for n in fib(6):
	# print(n)

# def odd():
	# print('1 step')
	# yield 1
	# print('2 step')
	# yield (3)
	# print('3 step')
	# yield(5)

# def add(x,y,f):
	# return f(x) + f(y)
# print(add(-5,-6,abs))

# from functools import reduce

# def str2int(s):
    # def fn(x, y):
        # return x * 10 + y
    # def char2num(s):
        # return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    # return reduce(fn, map(char2num, s))
# print('232')

# from functools import reduce

# def char2num(s):
    # return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

# def str2int(s):
    # return reduce(lambda x,y:x*10+y,map(char2num,s))
# print('232')


# def _odd_iter():
	# n = 1
	# while True:
		# n = n + 2
		# yield n

# def _not_divisible(n):
	# return lambda x: x%n > 0
	
# def primes():
	# yield 2
	# it = _odd_iter() #初始化序列
	# while True:
		# n = next(it) #返回序列的第一个数
		# yield n
		# it = filter(_not_divisible(n),it) #构造新序列

# for n in primes():
	# if n < 1000:
		# print(n)
	# else:
		# break

# def calc_sum(*args):
	# ax = 0
	# for n in args:
		# ax = ax + n
	# return ax
# print(calc_sum(10,10,10))

# def lazy_sum(*args):
	# def sum():
		# ax = 0
		# for n in args:
			# ax = ax + n
		# return ax
	# return sum

# f = lazy_sum(1,3,5,7,9)
# print(f)
# print(f())

# def count():
	# fs = []
	# for i in range(1,4):
		# def f():
			# return i*i
		# fs.append(f)
	# return fs

# f1,f2,f3 = count()
# print(f1(),f2(),f3())

# def count():
	# def f(i):
		# def g():
			# return i*i
		# return g
	# fs = []
	# for i in range(1,4):
		# fs.append(f(i))
	# return fs
# f1,f2,f3 = count()
# print(f1(),f2(),f3())

# f = lambda x: x*x
# print(f(5))

# def log(func):
	# def wapper(*args,**kw):
		# print('call %s():' % func.__name__)
		# return func(*args,**kw)
	# return wapper

# @log
# def now():
	# print('2015-3-25')

# now()

# import functools

# def log(text):
	
	# def decorator(func):
		# @functools.wraps(func)
		# def wapper(*args,**kw):
			# print('%s %s():'%(text,func.__name__))
			# return func(*args,**kw)
		# return wapper
	# return decorator

# @log('execute')
# def now():
	# print('2015-3-25')

# now()
# print(now.__name__)
















