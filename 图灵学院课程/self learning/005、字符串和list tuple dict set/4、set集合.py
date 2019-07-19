'''
集合：跟数学中集合的概念一致
    内容无序+内容不重复

'''
#集合的定义
#1、使用set  set里面只能放一个元素
sa=set()
print(sa)
li=[1,2,3,4,5,6,5,5,5]
sb=set(li)
print(sb)

#2、使用大括号
sc={4,8,9,1,2,2,2,3,3,5,5,6,5,78,657,4444}
print(sc)

#集合遍历
for i in sc:
    print(i)

#集合另一种遍历
sa={(1,2,3),(4,5,6),('i','love','wangxiaojing')}
for i,j,k in sa:
    print(i,j,k)

#集合的生成式
sa={1,2,3,4,5,6,7,8,9,7}
#利用sa生成一个sb
#集合内涵
sb={i for i in sa }
print(sb)
sc={i for i in sa if i%2 == 0}
print(sc)

#双重for循环 把sa 中的每一个元素的平方生成一个新的集合
#用一个for
sd={ i**2 for i in sa}
print(sd)


'''
集合的内置函数 类比前面的list tuple
len:长度
max/min:最值
add：向集合中添加元素
remove

'''
#添加元素
sa={1,2,3,4,5,6}
print(sa.add(7))#集合不能更改
print(sa)

'''
删除元素  remove 和discard 的区别
    remove:删除没有的元素会报错
    discard：删除没有的元素也不会报错
'''

sa.remove(5)
print(sa)

'''
pop弹出集合的一个内容
删除的内容是随机的
删除的内容没有规律

'''
sa={1,2,3,4,5,6,7}
print(sa)
sa.pop()
print(sa)


'''
集合的数学操作
    交集：intersection
    差集：difference  或者直接用减号
    并集：union
'''
sa={1,2,3,4,5}
sb={3,4,5,6,7,8,9}
print(sa.intersection(sb))
print(sa-sb)


'''
frozenset冰冻集合
    不允许修改的集合
    

'''
#案例
print(sa)
sb=frozenset(sa)
print(sb)