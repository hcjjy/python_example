from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self.capacity = capacity
	
	def __setitem__(self,key,value):
		containsKey = 0 if key in self else 1
		if len(self) + containsKey >= self.capacity:
			last = self.popitem(last = False)
			print('remove:',last)
		if not containsKey:
			del self[key]
			print('set:', (key,value))
		else:
			print('add:', (key,value))
		OrderedDict.__setitem__(self,key,value)
