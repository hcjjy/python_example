#!/usr/bin/env python3
# -*-coding: utf-8 -*-
'task_master.py' #文档注释
__autor__ = 'myth'

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()
#result_queue_copy = result_queue
def ret_task():
	global task_queue
	return task_queue
def ret_queue():
	global result_queue
	return result_queue
	
# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

if __name__ =='__main__':
	freeze_support()
	# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
	QueueManager.register('get_task_queue', callable=ret_task)
	QueueManager.register('get_result_queue', callable=ret_queue)
	# 绑定端口5000, 设置验证码'abc':
	manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
	# 启动Queue:

	manager.start()
	# 获得通过网络访问的Queue对象:
	task = manager.get_task_queue()
	result = manager.get_result_queue()#result_queue_copy
	# 放几个任务进去:
	for i in range(10):
		n = random.randint(0, 10000)
		print('Put task %d...' % n)
		task.put(n)
	# 从result队列读取结果:
	print('Try get results...')
	for i in range(10):
		r = result.get(timeout=10)
		print('Result: %s' % r)
	# 关闭:
	manager.shutdown()
	print('master exit.')