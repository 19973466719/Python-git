
class MyClass(object):
    def __init__(self):
        self.ia1 = 18

    def do_sth1(self):
        print(self.ia1)

    def do_sth2(self):
        print(self.ia2)

    def do_another(self):
        self.ia2 = 56

    def do_sth3(self):
        print(self.ia3)

mc = MyClass()

mc.ia3 = 3.14
print(mc.ia3)   
mc.ia3 = 19
print(mc.ia3)   
mc.do_sth3()    


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student('张三', 98)
s2 = Student('李四', 86)

s1.age = 18

print(s1.__dict__)
print(s2.__dict__)
