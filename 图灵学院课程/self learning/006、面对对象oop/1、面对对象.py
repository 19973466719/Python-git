'''
OOP:
    以模块化思想解决工程问题
    面向过程 vs 面向对象
    由面向过程转向面对对象
    例子，我要开一个学校，叫轻羽学院，主要讲少儿编程：
        教师
        学生
        班主任
        教室
        学校
常用名词：
    OO:面对对象
    ooa：分析
    ood：设计
    oop：编程
    ooI:实现
    ooa→ood->ooi
对象 vs 类：
    类：抽象，描述的是一个集合，侧重于共性
    对象：具象，描述的是个体
类的内容：
    动作，函数
    属性，变量
定义类：class 关键字
类命名：
    遵循大驼峰
    第一个字母大写

'''
#定义类
class Student():
    #此处定义一个空类
    #pass是关键字，表示占位用的，无意义
    pass
class StudentNoPass():
    pass

#定义一个对象
xiaobai=Student()

class PythonStudent():
    name = 'NoOne'
    age = 18
    course = 'Python'
    '''
    定义类中的函数
    一般有self关键字
    其余跟普通函数相同
    '''
    def giveMeMoney(self):
        print('show me money')
        return None

xiaobai=PythonStudent()
print(xiaobai.name)
print(xiaobai.age)
print(xiaobai.course)
print(xiaobai.giveMeMoney())

class Student():
    #name,age是类的变量
    #主义类的变量的定义位置与方法
    #不需要前缀
    name='北京图灵学院'
    age=18
    def fun(self):
        print('i love python')
        return None
    #self 的名称可以更改，不是关键字，只是一个形式参数，调用时不需要用关键字
    def sayHi(meme):
        print('i love meme')
#实例化
#作业：中文能否当做变量名称
二拿=Student()
print(二拿)
'''
self
    self可以用别的名称代替
    self不是关键字
    作用只是指代本身
    yaoyao调用fun函数时self自动
    默认实例作为第一个参数传入
'''
yaoyao=Student()
yaoyao.fun()
yaoyao.sayHi()


'''
类的变量与作用域
    类变量：是类自己的变量
    实例变量：属于实例的变量
    

'''
#以下例子说明 实例变量可以借用类的变量
class Students():
    #name,age是类的变量
    #主义类的变量的定义位置与方法
    #不需要前缀
    name='北京图灵学院'
    age=18
    def sayHi(self):
        print('i am {},I am {} years old'.format(self.name,self.age))
        return None
erjing=Students()
erjing.sayHi()



class Student2():
    #name,age是类的变量
    #注意：类的变量的定义位置与方法
    #不需要前缀
    name='北京图灵学院'
    age=18
    def sayHi(self,n,a):
        self.name='tuling'
        self.age=19
        print('i am {},I am {} years old'.format(self.name,self.age))
        return None
xiaoliu=Student2()
print(xiaoliu.sayHi('name',1))


'''
访问类的属性
在类里面如果强制访问类的属性
需要用__class__（注意左右两个下划线）
类方法：定义类的方法的时候，没有self参数

'''
class Students():
    #name,age是类的变量
    #主义类的变量的定义位置与方法
    #不需要前缀
    name='北京图灵学院'
    age=18
    def sayHi(self,n,a):
        self.name='tulingxueyuan'
        self.age=17
        print('i am {},I am {} years old'.format(self.name,self.age))
        return None


class Student3():
    name='dana'
    age=18

Student3.__dict__
yueyue=Student3
yueyue.__dict__
print(yueyue.name)



class A():
    name='dana'
    age=18
b=A.__dict__
print(b)





















