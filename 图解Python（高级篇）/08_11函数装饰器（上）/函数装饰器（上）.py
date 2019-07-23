
def log(func):
    def wrapper(*args, **kwargs):
        print("函数%s被调用了" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def add(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2

print(add(1, 2))

print(add.__name__) 
