'''
多继承的例子
子类可以直接用于父类的属性和方法，私有属性和方法除外
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
    def worked(self):
        print("working")
class SuperMan(Person,bird,Fish):
    def __init__(self,name):
        self.name = name

s = SuperMan("yueyue")

s.fly()
