#抽象 没有具体实现内容的方法成为抽象方法

class Animal():
    def sayHello(self):#抽象类规范了子类的行为
        pass

class Dog(Animal):

        print("闻闻对方的味道")


class Person(Animal):

        print("Kiss me")



d = Dog()
d.sayHello()


p = Person()
p.sayHello()

#抽象类的实现
import abc

#声明一个类并且制定当前类的元类 下列格式固定
class Human(metaclass=abc.ABCMeta):

    #定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink(self):
        pass

    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play(self):
        pass

