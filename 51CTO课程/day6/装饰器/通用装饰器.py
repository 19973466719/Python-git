def outer(func):
    def inner(*args,**kwargs):
        #添加修改功能
        print('************')

        func(*args,**kwargs)
    return inner
@outer
def say(name,age):
    print("myname is %s,I am %d years old"%(name,age))
say("sunck",18)