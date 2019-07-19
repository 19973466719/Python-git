
#int 取整是向上去整
age=3.25
print(int(age))
#判断是否为闰年
year=int(input('请输入一个年份:'))
if year%4==0 and year%100 !=0 or year%100==0 and year%400==0:
    print(str(year)+'是闰年')
else:
    print(str(year)+"不是闰年")

#给用户三次机会猜想我们的数字，并且给出提示大于A还是小于A，若三次机会用完则提示你猜错了

import random
secert=random.randint(1,100)#计算机生成一个随机数
times = 3 #初始化用户的次数是3 用来控制循环次数 当times
while times:
    num=input('请输入一个数字')
    if num.isdigit():
        tmp=int(num)
        if tmp == secert:
            print("你猜对了")
            break
        elif tmp<secert:
            print('你的数字太小了')
            #times=times-1
        else:
            print("你的数字太大了")
            #times=times-1
    else:
        print("请输入数字")
print("你的机会用完了")