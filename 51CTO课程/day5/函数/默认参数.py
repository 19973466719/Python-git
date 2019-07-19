'''
概念：调用函数时，如果没有传递参数，使用默认参数


'''



#要用默认参数，最后将其放在最后
def myprint(str,age=18):
    print(str,age)
myprint("kaige")