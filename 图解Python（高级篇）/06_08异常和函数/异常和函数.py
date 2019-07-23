

"""
def f1():
    print(1 / 0)

def f2():
    f1()

def f3():
    f2()

f3()
"""


def f1():
    print(1 / 0)

def f2():
    f1()

def f3():
    try:
        f2()
    except ZeroDivisionError as err:
        print(err)

f3()
