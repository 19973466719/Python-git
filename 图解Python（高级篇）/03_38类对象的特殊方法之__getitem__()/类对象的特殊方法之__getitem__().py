
class MyClass(object):
    pass

mc = MyClass()
# print(mc[3])    


class MyDict(object):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

md = MyDict()

md["one"] = 18
md["two"] = 32
print(md.data) 

print(md["two"]) 

del md["two"]
print(md.data)  
