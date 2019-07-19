#set:类似dict  只有key 没有value
#创建set 需要一个list或者tuple或者dict作为输入集合
#重复元素在set中会自动被过滤
s1=set([1,2,3,4,5])
print(s1)

s2=set((1,2,3,3,2,2))
print(s2)

s3=set({1:"good",2:"nice"})
print(s3)

s4=set([1,2,3,4])
s4.add(6)#不能添加列表 和 字典
print(s4)
s4.add((1,2,6))
print(s4)


#插入整个list，tuple，字符串，打碎插入  用update
s5=set([1,2,3,4,5])
s5.update([6,7,8])
print(s5)

#遍历
s7=set([1,2,3,4])
for i in s7:
    print(i)
#set 没有索引
for index,date in enumerate(s7):
    print(index,date)


s8=set([1,2,3])
s9=set([2,3,4])
#交集
a1=s8 & s9
print(a1)

print(type(a1))

#并集
a2=s8 | s9








