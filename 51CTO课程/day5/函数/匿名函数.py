'''
概念：不使用def定义，使用lambda来创建函数

特点：
1、lambda只是一个表达式，比较简单
2、lambda是一个表达式，不是代码块，只能做简单的逻辑
3、lambda有自己的命名空间


格式：lambda 参数1......参数n  ：expression

'''
sum=lambda num1,num2:num1+num2
print(sum(1,2))

