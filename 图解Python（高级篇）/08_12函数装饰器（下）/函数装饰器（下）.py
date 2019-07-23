
import functools

def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("函数%s被调用了" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log2
def add2(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2

print(add2(1, 2))

print(add2.__name__) 



def log3(month, day):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s%s, 函数%s被调用了" % (month, day, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log3('6月', '18日')
def add3(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2

print(add3(1, 2))
