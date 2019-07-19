'''
list列表：
    一组由有序数据做成的序列
    数据有先后顺序
    数据可以不是一类数据
    list的创建:
        直接创建，用中括号
'''
L1=[1,2,3,4,5]
l2=[1,2,3,'xiaojing','大拿']
print(l2)
print(L1)
print(type(l2))
print(l2.append(4))
print(l2)
'''
列表的常见操作:
    访问：
        使用下标操作，也叫索引
        列表的元素索引是从0开始
        用[]表示下标
    切片操作：
        对列表进行任意一段的截取
        截取之后，创建一个新的列表 原来的列表不变
'''
L1=[1,3,4,5,6,7]
print(L1[0])

#切片操作需要注意取值范围：左包括右不包括
#切片之后列表不变
#用id来判断是否为同一个变量
l2=[1,2,3,4,5,6,7,8,9]
l3=(l2[1:10])
print(l2[1:10])
print(l2)
print(id(l2))
print(id(l3))

#切片的下标为空  默认为0和最后一个 默认步长为1 [开始位置：结束位置：步长]
print(l2[:4])
print(l2[::1])
#数组的最后一个数字的小标为-1,负数表示从右到左 默认从左到右
#打印[6,7,8]
print(l2[-4:-1])
print(l2[-2:-5:-1])
list=[1,5,6,7,8,9]
print(list)

#双重列表循环
#k,v 的数量要等于list列表内的元素
a=[['one',1],['two',2],['three',3]]
#这个例子说明，k，v的个数应该跟解包出来的变量个数一致
for k,v in a:
    print(k,'---',v)


'''
列表内涵：list content
通过简单方法创作列表

'''
#for 创建
a=['a','b','c']
#用list a 创建一个list b
#下面的代码含义是，对于所有a中的元素，逐个放入新列表b中
b=[i for i in a]
print(b)


a=['a','b','c']
#用list a 创建一个list b
#下面的代码含义是，对于所有a中的元素，逐个放入新列表b中
b=[i*2 for i in a]
print(b)

'''
还可以过滤原来list中的内容放入新列表
比如原有列表a，需要把所有a中的偶数生成新的列表b


'''

a=range(1,11)
b=[i for i in a if i%2 == 0]  #后面的判断进行过滤
print(b)

a=[i for i in range(1,4)]
print(a)

b=[i for i in range(100,400) if i%100 == 0]
print(b)

#列表生成是可以嵌套,相当于两个for循环
c=[ m+n for m in a for n in b ]
print(c)
#上面代码跟下面代码等价
for m in a:
    for n in b:
        print(m+n,end=" ")
print()

#嵌套的列表生成式也可以用条件表达式
c=[ m+n for m in a for n in b if m+n<250 ]
print(c)


'''
列表函数：
    list 是可变的，因此进行操作后其地址还是一样，只是在原来的list进行操作
    append：插入一个内容，在末尾家人
    insert：指定位置插入
    del:删除
    pop:把最后一个元素拿出来，相当于删除
'''
a=[i for i in range(1,5)]
print(a)
a.append(100)
print(a)


#insert：指定位置插入 insert(index,data)，插入位置是index前面
print(a)
print(id(a))
a.insert(3,666)
print(a)
print(id(a))
last_num=a.pop()
print(last_num)
print(a)

#del是删除下标的值
print(id(a))
del a[2]
print(a)
print(id(a))


#remove：在列表中删除指定的值，如果删除的值没有在list中则会报错

print(a)
print(id(a))
a.remove(666)
print(a)
print(id(a))

#两个id值是一样的，说明，remove是在原list直接操作

# clear清空
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
'''
a=list()
a=[]
地址会变

'''

'''
reverse:翻转
    id地址不变
extend:扩展列表，两个列表，把一个直接拼接到后一个上


'''
a=[1,2,3,4,5]
b=[6,7,8,9,1]
a.extend(b)
print(a)

'''
count：查找列表中指定值或元素的个数
print(a)


'''
print(a)
a.append(8)
a.insert(4,8)
print(a)
a_len=a.count(8)
print(a_len)


'''
copy:拷贝，浅拷贝
#列表类型变量赋值实例
a=[1,2,3,4,5,666]
print(a)
list类型,简单赋值操作，是传地址
如果想要避免传址，则需要用copy函数

'''
a=[1,2,3,4,5,666]
print(a)
b=a#此时为传值

b[3]=777
print(a)
print(b)

b=a.copy()
print(a)
print(id(a))
print(id(b))
b[3]=800
print(a)
print(b)


#前拷贝和深拷贝的区别
#浅拷贝 列表内部的列表依然是同一个地址 copy函数值拷贝一层内容
a=[1,2,3,[10,20,30]]

b=a.copy()
print(id(a))
print(id(b))
print(id(a[3]))

print(id(b[3]))
a[3][2]=100
print(a)
print(id(a))
print(b)
print(id(b))
#深拷贝 使用特定工具



