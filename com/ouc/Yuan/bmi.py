#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('height(unit: m):')
height = real(s)
s = input('weight(unit:kg):')
weight = real(s)

bmi=weight/(height*height)
if bmi < 18.5 :
	print('过轻')
elif bmi <25.0 :
	print('正常')
elif bmi <28.0 :
	print('过重')
elif bmi <32.0 :
	print('肥胖')
else :
	print('严重肥胖')
