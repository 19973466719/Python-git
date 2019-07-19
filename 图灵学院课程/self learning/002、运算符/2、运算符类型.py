#算数运算符
#/     //    %   *  **
#除法  取整   取余     乘方


'''
逻辑运算符 是布尔值的运算
and:与
or：或
not：非
python里面没有异或
'''
a=True
b=True
c=False
bb=a and b
print(bb)

#短路问题案例1
aa=a or b and (a and b) #转换成1+....
print(aa)

#短路问题案例2
def a():
    print('a')
    return True
def b():
    print('b')
    return False
aaa=a() and b() #短路发生
print(aaa)

print('*'*20)

bbb=a() or b()   #从左到右
print(bbb)

#成员运算符
'''
用来检测一个值或者变量是否在某个集合
in
not in
'''
L=[1,2,3,4,5]
a=6
aa=a in L
print(aa)

#身份运算符
a=1
b=1000
aa=a is b
print(aa)
e=1000989888
d=1000989888
cc=e is d
print(cc)
print(id(a))
print(id(b))

'''
运算符优先级
小括号最先
乘方优先
其他的按四则运算

'''