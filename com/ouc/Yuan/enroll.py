# -*- coding: utf-8 -*-
def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

enroll('Sarah','F')

enroll('Bob','M',7)

enroll('Adam','M',city='Tianjin')

def add_end(L=[]):
	L.append('END')
	return L

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())
print(add_end())