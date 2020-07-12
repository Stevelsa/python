#Monte Carlo method
from random import random
from time import perf_counter
Darts=1000*1000
hits=0
start=perf_counter()
for i in range(Darts):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist < 1:
        hits+=1
pi=4*(hits/Darts)
print("pie equals {:.6f}".format(pi))
print("using {:.6f} seconds".format(perf_counter()-start))