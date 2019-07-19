'''
变量作用域
变量按作用范围限制
分类：按照作用域分类
    全局：在函数外部定义
    局部：在函数内定义
变量的作用范围：
    全局变量：在整个全局范围都有效
    全局变量在局部可以使用（即函数内部可以
    局部变量只能在局部范围使用
LEGB原则
    L（local）：局部作用域
    E 外部嵌套函数作用域
    G 函数定义所在模块作用域
    B python内部模块的作用域
    里面可以访问外面
'''


a1=100
def fun():

    print(a1)
    print('I am in fun')
    a2=99
    print(a2)
print(a1)
#不能 调用a2 print(a2)是错误的
fun()

'''
提升局部变量为全局变量
使用global

案例如下
'''

def fun():
    global b1
    b1=100
    print(b1)
    print('I am in fun')
    b2=99
    print(b2)

fun()
print(b1)



'''
globals,locals函数
可以通过globals 和locals 显示出局部变量和全局变量
参看以下案例

'''
a=1
b=2
def fun(c,d):
    e = 111
    print('Locals={}'.format(locals()))
    print('Globals={}'.format(globals()))
fun(100,200)

'''
eval()函数
把一个字符串当成一个表达式来执行，返回表达式执行后的结果
语法：
    eval(string_code,globals=None,locals=None)
exec与eval类似 但是不返回结果
'''
x=100
y=200
z1=x+y
z2=eval('x+y')
print(z1)
print(z2)

z2=exec("print('x+y:',x+y)")
print(z2)


import random
random.randint(1,5)
