'''
递归函数：直接或者间接调用自己
优点:简洁，理解容易
缺点:对递归深度有限制，消耗资源大
python中对递归有限制，超过限制报错
方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果
注意：一定要有结束条件
'''
#求阶乘
def funa(n):
    if n==1:
        return 1#结束条件
    else:
        return n*funa(n-1)

print(funa(5))

#斐波那契数列

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))

#汉诺塔
a='A'
b='B'
c='C'
def hano(a,b,c,n):
    if n==1:
        print('{} -- {}'.format(a,c))
        return None
    if n==2:
        print('{}--{}'.format(a,b))
        print('{}--{}'.format(a,c))
        print('{}--{}'.format(b,c))
        return None
    hano(a,c,b,n-1)
    print('{}--{}'.format(a,c))
    hano(b,a,c,n-1)
hano(a,b,c,2)
hano(a,b,c,3)

s='hello world'
b=s.find('o',4,10)
print(b)


x=0
def fun():
    global x#将变量为全局变量
    x+=1
    print(x)
    fun()
fun()