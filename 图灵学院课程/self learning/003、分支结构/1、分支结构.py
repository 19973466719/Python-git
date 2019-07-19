'''
分支结构
if表达式
if 条件：
    语句1
    语句2
    语句3
条件表达式的结果必须为布尔值   当结果为True时，则执行语句 
字符串的真假
只有空字符串才为假，其余为真
'''
a='I am so cool'
if a:
    print('yes')
else:
    print('no')

#双向分支
a=int(input('请输入你的成绩“：“'))
if a>90:
    print('优秀')
elif a>80:
    print('良好')
elif a>70:
    print('中')
elif a>60:
    print('平')
else:
    print('我没你这学生')