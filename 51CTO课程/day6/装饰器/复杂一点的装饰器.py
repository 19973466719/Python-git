def say(age):
    print("sunck is %d years old"%(age))


def outer(fun):
    def inner(age):
        if age<0:
            age=0
        fun(age)
    return inner
'''
@outer #相当于say=outer(say)
def say(age):
    print("sunck is %d years old"%(age))
'''

say=outer(say)
say(-10)
