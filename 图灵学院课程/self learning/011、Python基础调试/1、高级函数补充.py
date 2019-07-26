'''


zip

把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容

'''

#zip 案例
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(z)
print(type(z))
for i in z:
    print(i)



l3 = ["haha",'ypj','cxx']
l4 = [10,99,99]
z = zip(l3,l4)
for i in z:
    print(i)

l5 = [i for i in z]
print(l5)#此时为空 因为他在上一次遍历完了

'''

enumerate

跟zip功能比较像
对可迭代对象里的每一元素，配上一个索引，
然后索引和内容构成tuple类型

'''

l1 = [11,22,33,44,55,66]
em = enumerate(l1,start=1)

l2 = [i for i in em]
print(l2)#返回下标索引和内容 start控制开始

'''
collections模块
-namedtuple
-deque
'''
import collections

help(collections.namedtuple)

point = collections.namedtuple("point", ["x","y"])

p = point(11,22)
print(p.x)
print(p[0])
print(type(p))
print(point.__mro__)

print(isinstance(p, tuple))#判断其为谁的子类


'''

dequeue

比较方便的解决了频繁删除插入带来的效率问题

'''
from collections import deque

q = deque(["a",'b','c'])
print(q)

q.append('d')

print(q)
q.appendleft("x")
print(q)


'''
defaultdict
当读取到不存在的dict时，也不报错


'''

from collections import defaultdict
#help(collections.defaultdict)
#lamda表达式 如果没有 则直接返回字符串
func = lambda:"dana"

d2 = defaultdict(func)
d2["one"]=1
d2["two"]=2
print(d2)
print(d2["four"])

'''
Counter
统计字符串个数


'''
from collections import Counter

c = Counter("adewtgddddaaaaddd")
print(c)

s = ["crown", "is", 'is','is', "smart"]
c = Counter(s)
print(c)