'''
概念：把一个函数当做参数返回一个替代版的函数，本质为一个返回函数的函数。


'''

#简单的装饰器
def fun1():
    print('sunck is a ggod man')

#
def outer(fun):
    def inner():
        print("******")
        fun()
    return inner

#f是fun1的加强版本  调用inner等价于用fun1
f=outer(fun1)
f()
