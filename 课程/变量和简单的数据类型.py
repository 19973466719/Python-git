#合并拼接字符串
#用+号合并字符串
#eg
#first_name="yao"
#last_name="peijun"
#full_name=first_name+last_name
#print(full_name)
#使用制表符或换行符来添加空白
#用\t添加制表符   用\n添加换行符
#print("\tpython")
#print("python\nC\njava")
#print("\tpython\n\tC\n\tJAVA"
#删除空白  rstrip删除后面的空格， lstrip删除前面的空格，strip删除两端空格
#male_game=" python "
#print(male_game.strip())
#print(male_game.lstrip())
#Python中 **表示乘方 小数计算暂时忽略小数点后的位数
#a=3^2
#print(a)
#用str将非字符串值装换为字符串的值
#age=23
#message=("happy"+str(age)+"rd happy!")
## print(message)
#print(3+4)
#print(2+5)
#print(1+6)
#print(0+7)
#fa=7
#message=("我最喜欢的数字是"+str(fa))
#print(message)
#import this


#input 从外界获取变量的值 int 表示数字类型  float=浮点类型 str表示字符串
#num1=int(input("请输入一个数字"))
#num2=int(input("请再输入一个数字"))
#print("num1 + num2=",num1+num2)
#type查找变量类型
age=10
print(type(age))
#id 寻找变量地址
print(id(age))






#数据类型转换 int向下取整 float小数   如果有其他无用字符会报错 + -只有表示符号才有用
print(int(1.9))
print(float(1))
print(int("123"))
print(float("12.3"))
#print(int("abc")报错
#print(int("123abc")报错
print(int("+123"))







#数学功能
#返回数学的绝对值 abs
a1=-10
a2=abs(a1)
print(a2)

#比较两个数的大小  正确为1 错误为0
a3=100
a4=9
print((a3<a4)-(a3>a4))

#乘方运算 pow
print((a3)**(a4))
print(pow(2,5))

#round(x,[,n])返回浮点数x的四舍五入的值，n为保留机会小数 默认为整数
print(round(104.123))


#导入库  ceil 表示向上取整 floor 和int一样
import math
print(math.ceil(18.1))
print(math.floor(18.1))


#返回整数部分和小数部分 modf
print(math.modf(22.3))



#开方sqrt


import random
#随机数

#方法1
print(random.choice([1,4,5,6,2,3]))
print(random.choice(range(1,10,2)))
print(random.choice("sunck")) #会将字符串“sunck”看做 s u n c k


#random.randrange(start,stop,step)
#start为指定范围的开始值，包含开始值 默认0
#stop为指定范围的结束值，不包含结束值
#step 为步长 默认1
print(random.randrange(1,100,2))
print(list(range(1,5)))



#随机生成[0,1)的浮点数
print(random.random())


list=[1,2,3,4,5]
#将序列的所有元素随机排序
random.shuffle(list)
print(list)



#随机生成一个实数 范围为[3,9]
print(random.uniform(3,9))

#交互式赋值定义变量
number6=6
number7=7
print(number6,number7)

#相同式赋值定义变量
number3=number4=number5=1
print(number3,number4,number5)