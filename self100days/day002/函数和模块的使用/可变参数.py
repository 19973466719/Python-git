# *args表示可变参数
# 即在用add函数时可以传入任意个参数

def add(*args):
    total=0
    for val in args:
        total +=val
    return total
print(add(1,5,2,4,8,7,9,8))