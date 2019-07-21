#init 举例
class A():
    def __init__(self,name=0):
        print('haha')

a=A()

#__call__举例 当对象为函数时触发
class A():
    name = 'yao'
    def __init__(self):
        print("haha")

    def __call__(self):
        print( "我被调用了")
#__str__举例  当对象为字符串是调用
    def __str__(self):
        return 'yao pei jun'

a = A()
a()
print(a)


#__getattr__ 访问不存在属性时触发
class A():
    name = 'noname'
    age = 18
    def __getattr__(self,name):
        print("没找到呀没找到")

a = A()
print(a.name)
print(a.a)
print(A.name)



# __setattr__案例 设置类的属性时候调用
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性：{}".format(name))
        #以下语句会导致死循环

        #self.name = value
        #为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name,value)
p = Person()
print(p.__dict__)
p.python = 0
print(p.__dict__)

#__gt__比较大小
class Student():
    def __init__(self,name):
        self.name = name#此时调用时会打印出name的值


    def __gt__(self, other):
        print("haha,{0}会比{1}大吗？".format(self.name,other.name))#此时调用才会打印出name否则只能打印其地址
        print("haha,{0}会比{1}大吗？".format(self,other))#此时调用只能打印其地址
        return self.name > other.name
#字符串比较柜子 从第一个字符开始比较大小 按ASCII码
stu1=Student("one")
stu2=Student("two")
print(stu1>stu2)

'''
类和对象的三种方法
 实例方法
    - 需要实例化才能使用
 静态方法
    - 不需要实例化，通过类直接访问
 类方法
    -不需要实例化


'''

class Person:
    #实例方法
    def eat(self):
        print(self)
        print("eat")
    #类方法
        #类方法的第一个参数一般命名为cls
    @classmethod
    def play(cls):
        print(cls)
        print("playing")

    #静态方法
    #- 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("saying")

yueyue = Person()
#实例方法
yueyue.eat()
#类方法
Person.play()
yueyue.play()
#静态方法
yueyue.say()
Person.say()








