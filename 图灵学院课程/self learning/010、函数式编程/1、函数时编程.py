'''
函数式编程(FunctionalProgramming)

基于lambda演算的一种编程方式

程序中只有函数
函数可以作为参数，同样可以作为返回值
纯函数式编程语言： LISP， Haskell
Python函数式编程只是借鉴函数式编程的一些特点，可以理解成一半函数式一半Python

需要讲述

高阶函数
返回函数
匿名函数
装饰器
偏函数



'''

'''
lambda表示
函数：最大程度复用代码

    存在问题：如果函数很小、很短，则会造成啰嗦
    对于阅读者来说，造成阅读流程的被迫中断


- lambda表达式（匿名函数）：
    - 表达式，函数体想到简单
    - 不是一个代码块，仅仅是一个表达式
    - 可以有参数，有多个参数也可以，用逗号隔开
    - 只是一个表达式 没有return
'''
#“小”函数举例
def printA():
    print('AAAAAAAAAAAAAA')

printA()


'''
lambda表达式
1.以lambda开头
2.紧跟一定的参数
3.参数后用冒号和表达式主题隔开
4.只是一个表达式

'''
stm  = lambda x: 100*x
print(stm(100))


stm2 = lambda x,y,z:x+y+z
print(stm2(1,2,3))


'''
高阶函数
把函数作为参数使用的函数，叫高阶函数


'''
#变量可以赋值
a = 100
b = a
#函数名称就是一个变量
def funA():
    print('crown is cool')
funA()
funB = funA
funB()

'''
高阶函数举例
funA是普通函数，返回一个传入数字的100倍数字


'''
def fun1(n):
    return n*100
def fun2(n):
    return fun1(n)*3



print(fun1(5))
print(fun2(5))

#写一个高阶函数
def func(n,f):
    return f(n)*3
print(func(5,fun1))

'''
系统高阶函数--map
就是映射，即把集合或列表的函数，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合




'''
#有一个列表，对列表每一个元素乘以10，得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)

print(l2)

#利用map实现
def mu(n):
    return n*10
help(map)
l3 = map(mu,l1)
print(l3)
#map类型是一个可迭代的结构，所以可以使用for循环 迭代第二次就会返回空列表
#for i in l3:
  #  print(i)

l3 = [1,2,3,4,5,6,7]
l4 = [i for i in l3]
print(l4)#打印空值

'''
reduce

原意是归并，缩减
把一个可迭代对象最后归并成一个结果
对于作为参数的函数要求： 必须由两个参数，必须由返回结果
reduce([1,2,3,4,5]) == f( f(f(f(1,2),3), 4),5)
reduce 需要导入functools包



'''
from functools import reduce

def myfun(x,y):
    return x+y

a=reduce(myfun,[1,2,3,4,5,6] )
print(a)

'''
filter函数
- 过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表返回
- 更map相比较：
相同：都对列表的每一个元素逐一进行操作
不同：map会生成一个跟原来数据想对应的新队列
filter不一定，只要符合条件的才会进入新的数据集合
filter函数怎么写：
利用给定函数进行判断
返回值一定是个布尔值
调用格式： filter(f, data), f是过滤函数， data是数据
    



'''
l = [1,2,3,4,5,6,78,9]
l6 = [i for i in l if i%2 == 0]
print(l6)
help(filter)


def isEven(a):
    return a%2 == 0
l =[3,4,5,6,7,8,9,7,8]
rst = filter(isEven,l)
print(type(rst))
print(rst)
print([i for i in rst])

'''
高阶函数-排序
- 把一个序列按照给定算法进行排序
- key:在排序前对每一个key函数运算，可以理解成按照key函数定义的逻辑进行排序


'''
#案例1
a = [234,456,123,454,444,222]
al = sorted(a,reverse=True)#此时为倒叙 默认为顺叙
print(al)
#案例2
a =[-1, -2 ,8, -4, 9,5, 6]
al = sorted(a,key=abs)
print(al)

# 字符串排序案例
astr = ['Crown','crown','is','cool']

str1 = sorted(astr)

print(str1)

str2 = sorted(astr,key=str.lower)

print(str2)


'''
返回函数
返回具体的值
也可以返回一个函数


'''
#普通函数
def my(a):
    print("in my")
    return None

#函数作为返回值然后，返回的函数在函数体内定义

def my2():
    def my3():
        return 3
    return my3

f3 = my2()
print(f3)
print(type(f3))

print(f3())

'''
负责
args:参数列表
1 my4定义函数，返回内部的my5函数
2 my5用了外部my4的变量参数列表


'''
def my4(*args):
    def my5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return my5

f5 = my4(1,2,3,4,5,6,7,8)
print(f5())


'''
闭包
当一个函数在内部定义函数，
并且内部的函数应用外部函数的参数或者局部变量，
当内部函数被当做返回值的时候，
相关参数和变量保存在返回的函数中，这种结果，叫闭包
上面定义的my4是一个标准闭包结构


'''
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()

print(f1())
print(f2())
print(f3())
#返回三个9

'''
出现的问题：

造成上述状况的原因是,返回函数引用了变量i， i并非立即执行
，而是等到三个函数都返回的时候才统一使用，此时i已经变成了3，
最终调用的时候，都返回的是 3*3
此问题描述成：返回闭包时，返回函数不能引用任何循环变量
解决方案： 再创建一个函数，用该函数的参数绑定循环变量的当前值，
无论该循环变量以后如何改变，已经绑定的函数参数值不再改变
'''
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append((f(i)))
    return fs

f1,f2,f3 = count1()

print(f1())
print(f2())
print(f3())


'''
装饰器


'''
def hello():
    print("Hello world")

f = hello
#f和hello是一个函数
print(id(f))
print(id(hello))
print(f.__name__)

'''
# 现在由新的需求：
# 对hello功能进行扩展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改动现有代码
# ==>使用装饰器

'''

'''
装饰器(Decrator)

在不改动函数代码的基础上无限制扩展函数功能的一种机制，
本质上讲，装饰器是一个返回函数的高阶函数
装饰器的使用： 使用@语法， 
即在每次要扩展到函数定义前使用@+函数名

'''
import time
def printTime(f):
    def wrap(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrap

#上面定义了一个装饰器，使用时用@

@printTime

def hello():
    print("Hello world")

hello()

#装饰器的好处是，一旦定义，可以装饰任意函数
#装饰器的功能直接添加到定义函数的功能

@printTime

def hello2():
    print('Crown is cool')
hello2()


# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数

def hello3():
    print("我是手动执行")

hello3()
hello3 = printTime(hello3)
hello3()
f = printTime(hello3)
f()#打印出两个时间

'''
偏函数


'''
# 将8进制的字符串12345，表示成十进制
a=int("12345",base=8)
print(a)

a=int("12345",base=16)
print(a)

'''
偏函数
- 参数固定的函数，相当于一个由特定参数的函数体
- functools.partial，把一个函数的某些参数固定，返回一个新函数




'''
import functools
int16 = functools.partial(int,base=16)

print(int16("123"))

