
class MyClass(object):
    ca = "ca"

    def __init__(self):
        self.ia = "ia"

    def im(self):
        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

print(dir(MyClass))

print(dir(MyClass()))