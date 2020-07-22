# -*- coding: utf-8 -*-
def findMinAndMax(L):
	n = len(L)
	if n == 0:
		return (None,None)
	minL = L[0]
	maxL = L[0]
	for i in range(n):
		if L[i] > maxL:
			maxL = L[i]
		elif L[i] < minL:
			minL = L[i]
	return (minL,maxL)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')