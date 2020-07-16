# -*- coding: utf-8 -*-

#x = 12.34
#s = area_of_circle(x)
#print(s)

print(abs(100))
print(abs(-100))
print(max(1,2))
print(max(2,3,1,-5))

print(int('123'))
print(float('12.34'))
print(str(1.23))
print(bool(1))

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-99))