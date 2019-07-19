#list转换为set
t1=[1,2,3,4,5,3,4]
s1=set(t1)
print(s1)

#tuple转换为set
s2=(1,2,3,4,5,3,4)
s3=set(s2)
print(s3)

#set转换为list
s4=([1,2,3,4,5])
s5=list(s4)
print(s5)

#set转换为tuple
s6=[1,2,3,4,5,6]
s7=tuple(s6)
print(s7)


#最重要的是去重
l=[1,2,3,4,4,5,6]
l=list(set(l))
print(l)