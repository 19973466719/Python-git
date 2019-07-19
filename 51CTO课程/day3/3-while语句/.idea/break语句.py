'''
break语句：
作用：跳出for 和while循环
注意：只能跳出距离他最近的那一层循环

'''
for i in range (10):
    print(i)
    if i==5:
        break


num=1
while num<=10:
    print(num)
    if num==3:
        break#结束循环
    num+=1
else:
    print("good")#由于跳出循环不会执行
#注意：循环语句可以有else语句，break导致循环截止，不会执行else下面的语句

