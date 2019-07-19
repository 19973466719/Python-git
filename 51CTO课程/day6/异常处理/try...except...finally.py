'''try ... ... expect......finally
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
    .....
except 错误码 as e:
    语句n
finally:
    语句e
作用：无论t是否有错误都执行最后的语句
'''
try:
    print(1/0)

finally:
    print('必须执行我')
