temp=input("请输入一个零到一百整数：")
print(type(temp))
if temp.isdigit():
    temp=int(temp)
    if 1<= temp<=100:
        print("你好看")
    else:
        print("丑八怪")
else:
    print("你说丑八怪")