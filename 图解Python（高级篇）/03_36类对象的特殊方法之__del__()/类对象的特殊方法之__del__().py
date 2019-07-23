
class MyClass(object):
    def __del__(self):
        print("特殊方法__del__被调用")

mc = MyClass()
del mc