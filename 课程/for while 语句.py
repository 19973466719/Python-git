
#import random
#a=random.randint(1,10)
#n=0
#while n<3:
# number=(input('请输入数字:'))
# if number.isdigit():#判断是否为数字
  #  number=int(number)
   # if number==a:
#        print('猜对了')
#        break
  #  elif number>a:
       # print("大了")
#    else:
#        print('小了')
   # print('这个数是:',a)
 #else:
  #  print('你输入的不是数字')
# n+=1 #还剩几次机会
#else:
 #   print("三次机会用完了")
 #   print("这个数是:",a)
#循环
#while 循环
#break跳出整个循环并且不会执行else里面的语句
#continue 当continue符合是就直接跳过本次循环
#a=1
#while a<10:
    #a+=1
    #if a==5:
        #continue
   # print(a)
#for循环 ， for 迭代
#a="python"
#for i in a:
   # print(i)
#b=[1,2,3,4,5]
#for i in b:
  #  print(i*i,end=" ")
#d={'a':1,'b':2,'c':3}
#for i in d:
    #print(i)
#此时迭代的是字典的键 key
#for i in d.values():
   # print(i)
#d.values()
#dict.values(d)
#range(0,100,2) 前开后闭
#range(5)
#range(0,5)
#for i in range(5):
   # print(i)   # 0 1 2 3 4
#range(5,10)
#list(range(5,10,2))  #初始点 截止点 步长
a=0
while a<=100:
    if a%2==0:
        print(a)
    a+=1

for i in range(101):
    if i%2==0:
        print(i)








