from collections import Iterable
from collections import Iterator
'''
可迭代对象：可以直接作用与for循环的对象统称为可迭代对象
（interable）。可以用isinstance（）去判断一个对象是否是iterable对象
1.集合数据类型，如list、tuple、dict、set、string
2、是generator，包括生成器和带yield的generator function

'''
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance(2,Iterable))
#print(isinstance((x for x in range(10)),Iterable)
'''
#迭代器：不仅可以作用for循环，还可以被next（）函数不断调用并返回下一个值，直到最后出现一个stopIteration错误表示无法继续
#继续返回
#可以被next（）函数调用并不断返回下一个值的对象称为迭代器（iterator对象)

#可以用isinstance函数判断iterator对象
'''
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance(2, Iterator))


l=(x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

#转成Iterator对象
a=iter([1,2,3,4,5])
print(next(a))
print(next(a))

