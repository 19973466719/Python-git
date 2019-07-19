#for 循环
#简单图形打印
'''
打印以下图形
* * * *
* * * *
* * * *
* * * *

'''
#利用for循环
'''
for i in range(0,4):
    print("* * * * *")
'''
#利用双层for循环
for i in range(0,4):
    for j in range(5):
        #print 默认自动换行
        print("* ",'')
    print()#注意python中缩进的问题

'''
打印以下图形
* * * * *
*       *
*       *
* * * * *
1、利用for循环控制打印行
2、如果是第一行和最后一行，全部打印
3、其他行，判断打印列，如果第一列和第二列，则打印 *，否则打印空格
'''
for i in range(4):
    if i ==0 or i==3:
        print('* '*5)
    if i==1 or i==2:
        print('*       *')
#用双层for循环
for i in range(4):
    if i ==0 or i==3:
        print('* '*5)
    elif i==1 or i==2:
        for j in range(5):
            if j ==0 or j==4:
                print('* ')
            else:
                print('  ',end ='')
        print()#手动换行
'''
打印
*
* * 
* * *
* * * *
* * * * *
逐次换行
'''
for i in range(5):
    for j in range(i+1):#注意range改变范围
        print('* ',end='')
    print()

'''
打印
*
* *
*   *
*     *
* * * * *
'''
for i in range(5):

        for j in range(i+1):
            if i==4:
                print('* ',end='')
                continue
            #如果不是最后一行
            #j控制的是列的数字
            if j==0 or j==i:#控制列
                print('* ',end='')
            else:
                print('  ',end='')#控制列
        print()

'''
打印倒立三角
* * * * *
* * * *
* * *
* * 
*
'''
for i in range(5):
    for j in range(5-i):
        print('* ',end='')
    print()



for i in range(5):
    for j in range(5-i):
        if i==0:
            print('* ',end='')
            continue#继续上面i==0的循环
        if j==0 or j==4-i:
            print('* ',end='')
        else:
            print('  ',end='')
    print()


#打印三角形，正三角形
'''
     *
    * *
   * * *
  * * * *
 * * * * *
 为
*
* * 
* * *
* * * *
* * * * *
向右缩进一个到三角
'''
for i in range(6):
    for j in range(i+1):
        print(' ',end='')
    for m in range(6-i):
        print('* ',end='')
    print()



#水仙花数
for i in range(100,1000):
    temp=list(str(i))
    a=int(temp[0])
    b=int(temp[1])
    c=int(temp[2])
    if i==a**3+b**3+c**3:
        print(i)
'''
三色球问题 有红黄蓝三种颜色的球，其中红球3个，黄球3个 篮球6个，一次性拿出8个球，求其出现的球的颜色状况
'''
for red in range(0,4):
    for yellow in range(0,4):
        for blue in range(2,7):#因为至少两个篮球
            if red+yellow+blue ==8:
                print(yellow,red,blue)