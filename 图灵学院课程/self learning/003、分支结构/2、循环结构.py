'''
for循环
for 变量 in 序列：
语句1
语句2...

'''
stu_list=['王大燕','李美丽','王晓静']
for stu in stu_list:
    if stu=='王晓静':
        print('ni you')
    else:
        print('sorry')

'''
for else语句
打印列表中的同学，
如果没有在列表中，我们需要打印提示语句表示循环结束
'''


'''
break:无条件结束整个循环，循环猝死
continue：继续下一次循环
pass：占位符 ,代表这句话啥也不干，没有跳过的功能
'''
#break  确定是否包含7 确定就直接打印一个 出现了之后直接跳出循环
num_list=[1,2,3,4,5,6,7,8]
for i in num_list:
    if i==7:
        print(i)
        break
    else:
        print(i)

#continue 结束本轮循环，继续下一次循环
dig_list=[1,2,3,4,5,6,7,8,9,10]
for i in dig_list:
    if i%2==1:
        continue

    print(i)


#pass案例1 占位符
age=19
if age>19:
    pass
else:
    print("你还小")

#pass案例2
ages=[2,23,43,54,65,2]
for age in ages:
    pass
    print(age)

#range函数：生成有序数列 左闭右开 在Python中只有randint是列外


'''
#while循环：适用于不知道循环次数
while 条件表达式:
    语句1
else：
    语句2
  
'''
benqian=100000
year=0
while benqian<200000:
    benqian *=1.067
    year+=1

print(year)