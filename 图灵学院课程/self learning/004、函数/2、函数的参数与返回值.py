'''
参数：负责给函数传递一些必要的数据或者信息
形参：在函数定义的时候用到的参数没有具体值，只是一个占位符
实参：在调用函数的时候输入的值
返回值：调用函数的时候的一个执行结果
    使用 return 返回结果
    如果没有值需要返回，我们推荐使用return None
    函数一旦执行return，则函数立即结束
    如果函数没有return关键字，则函数默认返回None
    最好写return
    help函数查找


'''
def hello(person):
    print('{0},你好吗'.format(person))
    return None#person 只是一个占位符
p='小明'
hello(p)
pp=hello('yao')
print(pp)
help(format)


#打印九九乘法表
#1利用for循环
for i in range(1,10):
    for j in range(1,i+1):
        print(i*j,end='  ')
    print()
#2利用函数
def jiujiu():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}*{}={}" .format(i,j,i*j), end='  ')
        print()
    return None
#重复打印
jiujiu()
jiujiu()

#改造函数 利用嵌套函数
def printline(line_num):''''
line_num:行号
打印一行九九乘法表
'''

def jiujiu():
    for o in range(1,10):
        printline()
    return  None


