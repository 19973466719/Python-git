#自定义类
#自己组装一个类
#例1
class A():
    pass

def say(self):
    print("saying")

class B():
    def say(self):
        print("saying")
say(1)
a = say#函数名可以当变量使用 此时 a 和 say 代表同一个函数
a(1)

A.say = say#此时让A的类的say属性等于say函数
a = A()
a.say()

b = B()
b.say()


#组装例子2
from types import MethodType

class A():
    pass
def say(self):
    print("saying")
a = A()
a.say = MethodType(say,A)#时say加入到A中
a.say()



#help(type)
#利用type造一个类
def say(self):
    print("saying")

def talk(self):
    print("taking")

A = type('Aname',(object,),{"class_say":say,"class_talk":talk})
print(A)
a = A()
a.class_talk()
a.class_say()


'''
元类
元类写法是固定的，必须继承子type
一般以metaclass结尾


'''
class TulingMetaClass(type):
    #以下为固定
    def __new__(cls, name, bases, attrs):
        print("haha")
        attrs["id"] = '000000'
        attrs['addr'] = "北京"

        #自己的业务处理
        return type.__new__(cls, name, bases, attrs)

#元类定义为就可以使用
class Teacher(object,metaclass=TulingMetaClass):
    pass

t = Teacher()
print(t.id)
