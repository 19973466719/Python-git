
class MyClass(object):
    pass

mc = MyClass()

# print(mc.data)  
# mc.do_sth() 


class SomeClass(object):
    def __getattr__(self, name):
        if name == "data":
            return 18
        elif name == "do_sth":
            return print
        raise AttributeError("'SomeClass' object has no attribute '%s'" % name)

sc = SomeClass()
print(sc.data)  
sc.do_sth(1, 2, 3)  
# print(sc.score)
