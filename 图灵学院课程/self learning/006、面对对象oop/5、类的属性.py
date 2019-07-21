'''
属性案例
创建Student类，描述学生类
学生具有Student.name属性
但name格式并不统一


'''

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hai, my name is {0}". format(self.name))

    def setName(self,name):
        self.name
s1 = Student("Liu Ying", 19)
s2 = Student("michi Stangle" , 24)
s1.intro()
s2.intro()

'''
property案例
定义一个person类，具有name，age属性
对于任意输入的姓名，我们希望都用大写方式保存
年龄，我们希望内部统一用整数保存
x = property(fget,fset,tdel,doc)
'''
class Person():
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = 'NoName'

    name = property(fget,fset,fdel,"对name进行操作")

p1 = Person()
p1.name = 'tuling'
print(p1.name)
#年龄保存整数
class Person():
    '''
    crown is a nice man
    
    '''
    def fget(self):
        return self._age
    def fset(self,age):
        self._age =int(age)
    def fdel(self):
        self._age = 'NoName'

    age = property(fget,fset,fdel,"对name进行操作")

p1 = Person()
p1.age = 18.5
print(p1.age)

#类的内置属性
print(Person.__mro__)
print(Person.__dict__)
print(Person.__doc__)
print(Person.__bases__)

'''
属性的三种方法
赋值
读取
删除
'''
class A():
    def __init__(self):
        self.name = "haha"
        self.age = 18
    #此变量，就是对类变量读取操作时应该执行的函数功能
    def fget(self):
        print("我被读取了")
        return  self.name

    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self,name):
        print("我被写入了")
        self.name = "tulingxueyuan:" + name

    # fdel是删除变量进行的操作
    def fdel(self):
        pass
    '''
    property 的四个参数位置固定
    第一个代表读取是的函数
    第二个代表写入时需要调用的函数
    第三个是删除
    '''
    name2 = property(fget,fset,fdel,"这是一个property")



a = A()

print(a.name)
a.name2 = 'hahaha'
print(a.name2)