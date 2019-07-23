
class MyClass(object):
    def im1(self, p1, p2):
        print(p1, p2)

    def im2(self):
        self.im1(1, 2)

mc = MyClass()


def do_sth(self):
    print("do_sth()被调用了")

from types import MethodType
mc.do_sth = MethodType(do_sth, mc)
mc.do_sth()    


mc2 = MyClass()
# mc2.do_sth()  


def im3(self):
    print("im3()被调用了")

MyClass.im3 = im3

mc.im3()    
mc2.im3()   
