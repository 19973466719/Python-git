
class MyClass(object):
    def __init__(self):
        self.x = 1

    def do_sth(self):
        print("do_sth被调用")

mc = MyClass()

print(hasattr(mc, 'x'))         
print(hasattr(mc, 'do_sth'))    
print(hasattr(mc, 'y'))       

print(getattr(mc, 'x'))     

f = getattr(mc, 'do_sth')
f() 

# print(getattr(mc, 'y')) 
print(getattr(mc, 'y', 2))  

setattr(mc, 'z', 3)
print(getattr(mc, 'z'))

setattr(mc, 'z', 4)
print(getattr(mc, 'z')) 

delattr(mc, 'z')
print(hasattr(mc, 'z')) 