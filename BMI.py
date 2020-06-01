#BMI.py
try:
    leng,wght=eval(input("请输入身高(m)和体重(kg)数值，以逗号分开"))
    ind=eval(input("请选择判断标准，1 for WHO，2 for 国标"))
except :
    print("不是数值型")
bmi=wght/(leng**2)
print("bmi is {:.2f}".format(bmi))
if bmi< 18.5:
    print("偏瘦")
elif 18.5 <bmi < 25:
    print ("正常")
elif 25 < bmi < 30 :
    print ("偏胖")
elif bmi > 30:
    print ("肥胖")
else :
    print("logic error")
