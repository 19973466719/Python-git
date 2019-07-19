'''
tuple(元组）
    可以理解为一个不允许更改的列表
    tuple的创建
    1、直接用小括号
    

'''
#1、直接用小括号
ta=()
print(type(ta))
#特例当括号里面只有一个数字时 其类型为int
tb=(100)
print(type(tb))
tc=(100,)#此时为tuple
print(type(tc))
#2.直接用逗号
ta=100,
print(type(ta))
tb=100,200,300,#后面可以跟逗号
print(tb)
#3使用tuple定义 直接用tuple
ta=tuple()
print(ta)
a=[1,2,3,5,5]
print(tuple(a))

'''
tuple特征与list基本一致
    有序
    可以访问不可以被修改
    元素可以是任意类型

'''
#索引操作
la=['i','love','wangxiaojing']
print(la)
ta=tuple(la)
print(ta[2])

#tuple分片操作
print(ta[:])
print(ta[:2])

#元组的相加
ta=100,200,300
tb=('i','love','wangxiaojing')
tc=ta+tb
print(tc)

#tuple乘法
tc=tb*2
print(tc)

#tuple 成员检测 in /not in
print('wangxiaojing' in tb)

#元组遍历
for i in tb:
    print(i)
#元组的嵌套
ta=((10,20),('i','wangxiaojing'))
#访问元组中的每一个元素
#1、使用双层循环
for i in ta:
    print(i)
    for b in i :
        print(b)
#2、使用单层循环 注意：j,k的个数 要和元组内部的数量相同
for j,k in ta:
    print(j,k)

'''
常用元组函数
len：长度

max: 最大值

count：对某一个元素记数

index：某一元素所在位置第一个

python的特殊用法 对元素互换
a=100
b='wang xiaojing'
a,b=b,a
'''