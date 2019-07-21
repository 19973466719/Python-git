class A():
    name='dana'
    age=18

    def say(self):
        self.name='aaaa'
        self.age=18
#此时A为类实例
print(A.name)
print(A.age)
print('*'*20)
print(id(A.age))
print(id(A.name))

a=A()
print(A.__dict__)
print(a.__dict__)

a.name = 'youga'
a.age=19
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.age))
print(id(a.name))


class Student ():
    # name,age是类的变量
    # 主义类的变量的定义位置与方法
    #不需要前缀
    name='北京图灵学院'
    age=18
    def say(self):#self 可以更改 只是一个参数，不是关键字
        self.name = 'tulingxueyuan'
        self.age = 17
        print('i am {},I am {} years old'.format(self.name,self.age))
    def sayagain(selfs):
        print('i am {},I am {} years old'.format(selfs.name,selfs.age))
A=Student()
print(A.say())
print(A.sayagain())


class Teacher():
    name='dana'
    age=19
    def say(self):
        self.name="youga"
        self.age=17
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(__class__.age))#此时用的是字典内的属性
    def SayAgain():#此时为绑定类的方法 只能用类本身调用
        print(__class__.name)
        print(__class__.age)
        print("hello,nice to meet you")

t=Teacher()
t.say()

Teacher.SayAgain()




# 关于self的案例

class A():
    name='liuying'
    age=18
    def __init__(self):
        self.name='aaaa'
        self.age=200
        print('I am TULING')


    def say(self):
        print(self.name)
        print(self.age)
class B():
    name='bbbb'
    age=90

a=A()
#此时系统默认将啊作为第一个参数传入函数
a.say()

#此时，self被a替换
A.say(a)
#此时，传入的是类实例B，因为B具有name和age属性，所有不会报错
A.say(B)

#以上代码，利用了鸭子模型




