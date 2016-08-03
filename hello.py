# -*- coding: utf-8 -*-
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
















