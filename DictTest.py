class A(dict):
	id = 1;
	bd = 2;
	def __init__(self,**kw):
		super(A,self).__init__(**kw)
	
	def __getattr__(self,key):
		return self[key]

a = A(id1 =2,bd =3)
print(a.id1,a.bd)