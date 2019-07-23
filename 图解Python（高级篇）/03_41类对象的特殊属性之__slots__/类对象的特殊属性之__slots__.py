
class MyClass(object):
    __slots__ = ("attr1", "do_sth1")

mc = MyClass()

mc.attr1 = 18

# mc.attr2 = 56   

def do_sth1(self):
    print("do_sth1被调用了")

from types import MethodType
mc.do_sth1 = MethodType(do_sth1, mc)
mc.do_sth1()

def do_sth2(self):
    print("do_sth2被调用了")

# mc.do_sth2 = MethodType(do_sth2, mc)



# print(MyClass().__dict__)



class MyChildClass1(MyClass):
    pass

mcc1 = MyChildClass1()

mcc1.attr3 = 56

class MyChildClass2(MyClass):
    __slots__ = ("attr2", "do_sth2")

mcc2 = MyChildClass2()

mcc2.attr1 = 18
mcc2.attr2 = 18
mcc2.do_sth1 = 18
mcc2.do_sth2 = 18

# mcc2.attr3 = 18
