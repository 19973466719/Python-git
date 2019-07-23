import random
a=random.randint(1,10)

number=(input('请输入数字:'))
if number.isdigit():
    number=int(number)
    if number==a:
        print('猜对了')
    elif number>a:
        print("大了")
    else:
        print('小了')
    print('这个数是:',a)
else:
    print('你输入的不是数字')