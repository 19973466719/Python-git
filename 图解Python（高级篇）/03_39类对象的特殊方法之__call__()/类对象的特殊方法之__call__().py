
class MyClass(object):
    def __call__(self, *args, **kwargs):
        print(args, kwargs)

mc = MyClass()
mc()
mc(1, 2, x = 3, y = 4)



print(callable(print))  

def do_sth():
    pass

print(callable(do_sth)) 

print(callable(MyClass()))  

