'''
能处理比定义时更多的参数
'''

#加了*号的变量会存放所有未命名的变量参数，如果没有指定参数，就是一个空的元祖 代表元祖

def fuc(name,*args):
    print(name)
    print(type(args))
    for x in args:
        print(x)
fuc("sunck","good")


def sum(*l):
    sum=0
    for i in l:
        sum+=i
    return sum
print(sum(1,2,3,4))


#**代表 键值对的参数字典
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(x=1,y=2,z=3)



def func3(*args,**kwargs):
    pass#代表一个空语句