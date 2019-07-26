'''
多继承的例子
子类可以直接用于父类的属性和方法，私有属性和方法除外
object 是所有类的父类
'''


class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print('i am swiming')

class bird():
    def __init__(self,name):
        self.name=name

    def fly(self):
        print("I am flying")

class Person():
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
#多继承的例子
class SuperMan(Person,bird,Fish):
    def __init__(self,name):
        self.name = name
#单继承的例子
class SwimMan(Person):
    def __init__(self,name):
        self.name=name
stu=Person("pengpeng")
print(stu.get_name())


s = SuperMan("yueyue")

s.fly()

#菱形问题
class A():
    name=19
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
a=A()

print(issubclass(B,A))#判断是否一个类是另一个类的子类
print(isinstance(a,A))#判断是否为实例
print(hasattr(A,'age'))#检测是否成员在类中
#print(getattr())
print(setattr(A,'name',18))
print(A.name)
print(dir(A))#获取对象的成员列表
print(getattr(A,'name',18))
class Person():
    #对面Person类进行实例化的时候
    #姓名要确定
    #年龄得确定
    #地址肯定有
    def __init__(self):
        self.name = "NoName"
        self.age = 18
        self.address = "studentwho"
        print("In init func")

'''
Mixin 案例

'''
class Person():
    name = 'yao'
    age = 18
    def sleep(self):
        print('sleeping')
    def eat(self):
        print('eat')
    def dirink(self):
        print('drink')

class Teacher(Person):
    def work(self):
        print('work')
class Student(Person):
    def study(self):
        print('study')


class Tutor(Teacher,Student):
    pass
t=Tutor()
print(Tutor.__mro__)#
print(t.__dict__)
print(Tutor.__dict__)
print("*"*20)

class TeacherMixin():
    def work(self):
        print("work")

class StudentMixin():
    def study(self):
        print("study")

class TutorM(Person,TeacherMixin,StudentMixin):
    pass


tt=TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)
tt.work()
