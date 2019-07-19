'''
传递值：传递的不可变类型
string、tuple、number 是不变的
'''
def func1(num):
    print(id(num))
    num=10
    print(id(num))




temp=20
func1(temp)
print(temp)





'''
引用传递：传递的是可变类型
list、dict   set 是可变的
'''
def func2(list):
    list[0]=100
lis=[1,2,3,4,5]
func2(lis)
print(lis)
