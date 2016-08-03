#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'sql Object Relational Mapping'# doc comment
__autor__ = 'myth'

#导入：
from sqlalchemy import Column,Integer,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类：
Base = declarative_base()

#定义User对象：
class User(Base):
	#表的名字：
	__tablename__= 'User'
	
	#表的结构：
	id = Column(Integer,primary_key = True)
	name = Column(String(20))
	
	#一对多：
	books = relationship('Book');

class Book(Base):
	__tablename__='Book'
	
	id = Column(Integer,primary_key =True)
	name = Column(String(20))
	#"多"的一方的book表是通过外键关联到user表的
	user_id = Column(Integer,ForeignKey(User.id))
	
#初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
#创建DBSession类型：
DBSession = sessionmaker(bind = engine)


#创建session对象：
session = DBSession()

#创建新User对象：
new_user = User(id=3,name = 'Bob')
#创建Book对象:
new_book = Book(id =1005,name = 'sdxl',user_id = 3)
new_book1 = Book(id =2003,name = 'xyj',user_id = 3)
new_book2 = Book(id =3004,name = 'xjqxz',user_id = 3)
#添加到session:
session.add(new_user)
session.add(new_book);
session.add(new_book1);
session.add(new_book2);
#提交即保存到数据库:
session.commit()

#关闭session
session.close()



#创建Session：
session = DBSession()
#创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行：
user = session.query(User).filter(User.id ==3).one()
#答应类型和对象的name属性：
print('type:', type(user))
print('name:',user.name)
for book in user.books:
	print('name:',[book.id,book.name])
#关闭Session：
session.close()



# create table User(
	# id int not null auto_increment primary key,
	# name varchar(20) not null
# )engine = InnoDB;

# create table Book(
	# id int not null auto_increment primary key,
	# name varchar(20) not null,
	# user_id int not null,
	# foreign key foreignName(user_id) 
	# references User(id)
# )engine = InnoDB;





























