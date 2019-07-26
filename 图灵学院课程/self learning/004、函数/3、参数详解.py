'''
参数分类：
    普通分类/位置参数
    默认参数
    关键字参数
    收集参数
    
'''
#普通参数案例
def normal_para(one,two,three):
    print(one+two)
    return  None
normal_para(1,2,2)

#形参与实参个数要相等


#默认参数案例
def default_para(one,two,three=3):
    print(one+two)
    return None
default_para(1,2)


#关键字参数
def keys_para(one,two,three):#不需要参数的顺序位置对应
    print(one+two)
    print(three)
    return None

keys_para(one=1,two=2,three=3)

'''
收集参数
把没有位置，不能定义时的参数位置相对应的参数，放入一个特定的数据结构中
语法：
    def func(*args)
        fun_body
        可以按照list使用方式访问args得到传入的参数
    调用：
    func(p1,p2,p3,...)
    可以不用args，
    参数名前必须加*
    收集参数可以和其他参数共存
    收集参数代码
    args看作一个list
    args为整个函数的区域都有
'''
def stu(*args):
    print('hello,大家好，我的自我介绍如下')
    print(type(args))
    for i in args:
        print(i)
stu('liuying','18','wangxiaojing')
#如果没有参数，则是一个空的元组

'''
收集参数之关键字参数
把关键字参数按字典格式存入收集参数
语法：
    def fun(**kwargs):
        fun_body
    调用：
    fun(p1=v1,p2=v2,...)
    kwargs默认
    调用的时候吧多远的参数放入kwargs
    访问时需要按字典格式

'''
def stu(**kwargs):
    print('hello,大家好，我的自我介绍如下')
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(k,'****',v)
stu(name='liuying',age='18',lover='wangxiaojing')
