#if -else 语句

#if-elif-else
'''
if 表达式1:
    语句1
elif 表达式2：
    语句2
...
else 表达式3：
    语句3
'''
#逻辑：直到某个表达式为真时 执行
age=int(input())
if age<0:
    print('未出生')
elif age<=3:
    print("婴儿")
elif age<=6:
    print("童年")
elif age<=18:
    print("青年")
else:
    print("成年人")
#每个el都是对上面所有表达式的否定


