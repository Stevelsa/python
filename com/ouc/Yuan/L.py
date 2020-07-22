# -*- coding: utf-8 -*-
L = []
n = 1
while n <= 99:
	L.append(n)
	n = n + 2

print(L)


L = ['Michael','Sarah','Tracy','Bob','Jack']
print(L)

r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)

print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])



L = list(range(100))
print(L)
print(L[:10])
print(L[::5])