'''
if语句格式
if 表达式：
    语句
逻辑 ： 当程序执行到if语句时，首先计算“表达式”的值，如果“表达式”的值为真，那么执行if的语句，如果表达式为假，
则跳过整个if语句继续向下执行

何为真假
假：0   0.0   ''    none  False
真： 除了假都是真
'''
num1=20
num2=20
if num1==num2:
    num1=100
print(num1)

'''
if else 语句
if 表达式：
    语句1
else：
    语句2
若表达式为真时，则进行语句1 若为假则进行语句二


'''
'''
num=int(input("请输入一个三位数"))
a=num %10  取各位数
b=num // 10% 10  取十位数
c=num // 100   取百位数
if num ==a**3+b**3+c**3:
    print("是")
else:
    print("不是")
三个数中最大数
'''
num1= int(input())
num2= int(input())
num3= int(input())
max=num1
if num2>num1:
    max=num2
if num3>max:
    max=num3
print("max=", max)
