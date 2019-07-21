class person():
    # name是共有的成员
    name = 'liuying'
    __age = 18#私有变量

a=person()
print(a.name)
a._person__age = 19
print(a._person__age)
print(person.__dict__)

#继承的语法
#在python中，任何类都要一个共同的父类叫object
#子类和父类同时定义同一个变量，则优先使用子类名称
class person():
    name = "NoName"
    __age = 0  #私有
    _petname = 'sec'#小名，是保护的，子类可以用
    def sleep(self):
        print('sleeping... ...')


#父类写在括号内
class Teacher(person):
    teacher_id = '9527'
    name = 'dana'
    def make_test(self):
        print('attention')
    pass


A=Teacher()
a=person()
print(A.name)
#print(A.__age)#私有的不能调用

A.sleep()
print(A._petname)#保护的能调用

#子类可以扩充父类的案例
class person():
    name = "NoName"
    __age = 0  # 私有
    _petname = 'sec'  # 小名，是保护的，子类可以用
    def sleep(self):
        print('sleeping... ...')
    def work(self):
        print('make some money')


# 父类写在括号内
class Teacher(person):
    teacher_id = '9527'
    name = 'dana'

    def make_test(self):
        print('attention')
    def work(self):
        #扩充父类的功能只需要先调用父类相同的函数，再添加新的功能
        #person.work(self)
        #另一种方法
        #super
        #person.work(self)
        super().work()
        self.make_test()
    pass
t = Teacher()
t.work()






'''
构造函数的概念
__init__就是构造函数
每次实例化的时候第一个被调用
因为主要工作是进行初始化，所有得名

'''
class Dog():
    def __init__(self):
        print('I am init in dog')

kaka = Dog()


'''
继承中的构造函数
'''
class Animal():
    pass
class PaxingAni(Animal):
    def __init__(self,name):
        print('paxing dongwu {}'.format(name))
        print(name)

    pass
class Dog(PaxingAni):
    def __init__(self):

        print('I am init in dog ')
#实例化时候，自动调用dog的构造函数，因此不再查找父类的构造函数
class Cat(PaxingAni):
    pass
kaka = Dog()
pipi = Cat(name='xiaoha')#此时的参数要和构造函数中的参数相对应


print(type(super))
help(super)


class A():
    pass


class B(A):
    pass

print(A.__mro__)
print(B.__mro__)












