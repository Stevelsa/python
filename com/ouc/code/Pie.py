#Pie.py
pi=0
i=0
for i in range(1000):
    pi+=1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
print("pie equals {:.12f}".format(pi))