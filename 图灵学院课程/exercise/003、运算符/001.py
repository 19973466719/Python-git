#x=1 y=2 z=3 如何将他们三个值交换
x=1
y=2
z=3
print(x)
print(y)
print(z)
x,y,z=z,x,y
print(x)
print(y)
print(z)
#
while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
#写循环时不要重复
i=0
str='iLoveTuling'
leng=len(str)
while i < leng:
    print(i)
    i+=1
#设计一个验证用户密码程序，用户只有三次机会，如果用户输入的内容包括‘*“”'则不算
password='123456'
times=3
while times:
    input_password=input('请输入密码')
    if "*"in input_password:
        print("不能有*号")
    elif input_password==password:
        print("密码正确")
        break
    else:
        times=times-1
print('你的机会用完了')