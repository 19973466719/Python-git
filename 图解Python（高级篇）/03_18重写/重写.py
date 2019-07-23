
class ParentClass(object):
    ca = "ca（父类）"

    def __init__(self):
        print("__init__()被调用了（父类）")

    def im(self):
        print("im()被调用了（父类）")

    @classmethod
    def cm(cls):
        print("cm()被调用了（父类）")

class ChildClass(ParentClass):
    ca = "ca（子类）"

    def __init__(self):
        super().__init__()
        print("__init__()被调用了（子类）")

    def im(self):
        super().im()
        print("im()被调用了（子类）")

    @classmethod
    def cm(cls):
        super().cm()
        print("cm()被调用了（子类）")

cc = ChildClass()

print(ChildClass.ca)    
print(cc.ca)     

cc.im()             

ChildClass.cm()        
cc.cm()      