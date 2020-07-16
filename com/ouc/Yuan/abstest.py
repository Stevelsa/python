import math


def quadratic(a, b, c):
	s = b*b - 4*a*c
	x1 = (-b + math.sqrt(s)) / (2*a)
	x2 = (-b - math.sqrt(s)) / (2*a)
	return x1, x2

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

def nop():
	pass