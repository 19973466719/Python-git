from random import randint
def roll_dice(n=2):
    '''
    
    :param n:色子的个数
    :return: n颗色子点数之和 
    '''
    total=0
    for _  in range(n):
        total +=randint(1,6)
    return total
def add(a=0,b=0,c=0):
    return a+b+c
# 没有指定参数默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))


print(add())
print(add(a=1,b=2,c=3))
