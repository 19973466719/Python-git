
class MyClass(object):
    def im1(self, p1, p2):
        print(p1, p2)

    def im2(self):
        self.im1(1, 2)

mc = MyClass()

mc.im1(1, 2)    
mc.im2()    
