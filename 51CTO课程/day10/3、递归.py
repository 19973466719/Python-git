
'''
递归调用:一个函数调用自身
递归函数：调用自身的函数

凡是循环能干的事，递归都能干。

'''
'''
方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果
'''

#输入一个数（大于等于一），求1+2+3+..+n
def sum(n):
    sum=0
    for x in range(1,1+n):
        sum+=x
    return sum
res=sum(6)
print("sum=",res)

'''
1+2+3+4+5+6
sum2(1)+2=sum2(2)
sum2(2)+3=sum2(3)
sum2(3)+4=sum2(4)
sum2(4)+5=sum2(5)

'''
def sum2(n):
    if n==1:
        return 1
    else:
        return n * sum2(n-1)
res=sum2(5)
print("res=",res)















