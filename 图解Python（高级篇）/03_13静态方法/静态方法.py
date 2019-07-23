
class MyClass(object):
    @staticmethod
    def sm(p1, p2):
        print(p1, p2)

    @classmethod
    def cm(cls):
        MyClass.sm(1, 2)
        cls.sm(1, 2)

    def im(self):
        self.sm(1, 2)

MyClass.sm(1, 2)    

mc = MyClass()

mc.sm(1, 2)   

MyClass.cm()
mc.im()
