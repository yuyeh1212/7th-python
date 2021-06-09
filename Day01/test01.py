# 判斷是否擁有投票權
age = int(input("please enter your age:"))
if age >= 18:
    print('恭喜擁有投票資格')
else:
    print('尚未擁有資格還需等{}年'.format(18 - age))
