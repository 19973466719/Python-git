'''
append
extend
insert

'''
a=[1,2,3,4,5]
a.append([6,7,8])#在末尾添加目标[6,7,8]
print(a)

b=[1,2,3,4,5]
b.extend([6,7,8])#直接将后面添加元素6,7,8
print(b)

c=[1,2,3,4,5]
c.insert(3,10)
print(c)

member = ["crown", "is", "handsome"]

#如何将下边这个列表的“图灵学院”修改为“周老师”
ls = [1,[1,2,["图灵学院"]],3,5,8]

#对列表修改
ls[1][2][0] = "周老师"
print(ls)

#将l = [(x,y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0还原
#上式等价双重for循环
l=[]#首先定义一个空列表
for x in range(0,10):
    for y in range(0,10):
        if x%2 == 0 and y%2 !=0:
            l.append((x,y))

print(l)




