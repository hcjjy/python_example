#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
'an test module'  #文档注释

__autor__ = 'heqinghui'

# import sys

# def test():
	# args = sys.argv
	# if len(args)==1:
		# print('Hello,World!')
	# elif len(args)==2:
		# print('Hello,%s!' % args[1])
	# else:
		# print('Too many arguments')

# if __name__=='__main__':
	# test()
	
# class Student(object):
	# def __init__(self,name,score):
		# self.name = name
		# self.score = score
		
	# def print_score(self):
		# print('%s: %s' %(self.name,self.score))

# bart = Student('Bart',59)
# lisa = Student('Lisa',87)
# bart.print_score()
# lisa.print_score()

# class Student(object):
	# def __init__(self, name='heqinghui', score = 69):
		# self.__name = name
		# self.__score__ = score
	# def print_score(self):
		# print('%s: %s' % (self.__name, self.__score__))
		
	# def get_grage(self):
		# if self.__score__ >= 90:
			# return 'A'
		# elif self.__score__ >= 60:
			# return 'B'
		# else:
			# return 'C'

# bart = Student('test',33)
# bart.__name='qing'
# bart.__score__ = 99		
# bart.print_score()
# print(bart.get_grage())

# class Student(object):

    # def get_score(self):
         # return self._score

    # def set_score(self, value):
        # if not isinstance(value, int):
            # raise ValueError('score must be an integer!')
        # if value < 0 or value > 100:
            # raise ValueError('score must between 0 ~ 100!')
        # self._score = value


# class Student(object):
    # @property
    # def score(self):
        # return self._score
    # @score.setter
    # def score(self, value):
        # if not isinstance(value, int):
            # raise ValueError('score must be an integer!')
        # if value < 0 or value > 100:
            # raise ValueError('score must between 0 ~ 100!')
        # self._score = value


# class Student(object):
	# @property
	# def birth(self):
		# return self._birth
	# @birth.setter
	# def birth(self,value):
		# self._birth = value
	# @property
	# def age(self):
		# return 2016 - self._birth
# class Mammal(object):
	# pass
# class RunnableMixIn(object):
	# pass
# class CarnivorousMixIn(object):
	# pass
# class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
	# pass
# print(len(RunnableMixIn))

# class Student(object):
	# def __init__(self,name):
		# self.name = name
	# def __str__(self):
		# return 'Student object (name: %s)' % self.name
	# __repr__ = __str__
	
# class Fib(object):
	# def __init__(self):
		# self.a, self.b = 0,1
	# def __iter__(self):
		# return self
	# def __next__(self):
		# self.a, self.b = self.b, self.a + self.b
		# if self.a >100000:
			# raise StopIteration()
		# return self.a
	# def __getitem__(self,n):
		# if isinstance(n,int):
			# a,b = 1,1
			# for x in range(n):
				# a,b = b, a+b
			# return a
		# if isinstance(n,slice):
			# start = n.start
			# stop = n.stop
			# if start is None:
				# start = 0
			# a,b = 1,1
			# L = []
			# for x in range(stop):
				# if x >=start:
					# L.append(a)
				# a,b = b, a+b
			# return L

# for n in Fib():
	# print(n)

# class Chain(object):
	# def __init__(self,path =''):
		# self._path = path
	# def __getattr__(self,path):
		# if path =='users':
			# return lambda name:Chain('%s/%s' %(self._path,':users'))
		# return Chain('%s/%s' %(self._path,path))
	# def __str__(self):
		# return self._path
	# __repr__ = __str__

# from enum import Enum,unique

# @unique
# class Weekday(Enum):
	# Sun = 0
	# Mon = 1
	# Tue = 2
	# Wed = 3
	# Thu = 4
	# Fri = 5
	# Sat = 6

# class ListMetaclass(type):
	# def __new__(cls,name,bases,attrs):
		# attrs['add'] = lambda self,value:self.append(value)
		# return type.__new__(cls,name,bases,attrs)

# class MyList(list,metaclass = ListMetaclass):
	# pass


class Field(object):
	def __init__(self,name,column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s:%s' %(self.__class__.__name__,self.name)

class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if (name =='Model'):
			return type.__new__(cls,name,bases,attrs)
		print('Found model:% s' %name)
		mappings = dict()
		for k,v in attrs.items():
			if isinstance(v,Field):
				print('Found mappings: %s ==> %s' % (k,v))
				mappings[k] = v
		for k in mappings: #删除类属性，防止副作用
			attrs.pop(k)
		attrs['__mappings__'] = mappings #保存属性和列的映射关系
		attrs['__table__'] = name #假设表名和类名相同
		return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass = ModelMetaclass):
	def __init__(self,**kw):
		super(Model,self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute'%s'" % key)
	def __setattr__(self,key,value):
		self[key] = value
	def save(self):
		fields = []
		params = []
		args = []
		for k,v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self,k,None))
		sql = 'insertt into %s (%s) values (%s)' %(self.__table__,','.join(fields),','.join(params))
		print('SQL:%s' %sql)
		print ('ARGS:%s' %str(args))

class User(Model):
	#定义类的属性到列的映射
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	passwd = StringField('password')
		
	
#创建一个实例ORG,一行映射一个对象，一个类对应一个表
u = User(id = 12345,name='Michael',email='test.org',password='huihui')
u.save()







