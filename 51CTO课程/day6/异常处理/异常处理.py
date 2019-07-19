'''
print(3/0)

'''
#需求：当程序遇到问题时不让程序错误，而越过错误继续向下执行

'''try ... ... expect......else
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
else:
    语句e
    
    
注意：else语句可有可无

作用：用来检测try语句中的错误，从而让except语句捕获错误信息并处理

逻辑：当程序执行到try-except-else语句
1、

'''




#使用except而不使用任何的错误类型
try:
    print(4/0)
except:
    print('程序错误')


#使用except带着多种异常
try:
    print(4/0)
except ("错误1，错误2“"):
    print("出现了错误1或错误2")
