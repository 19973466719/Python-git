def ca(x,y):
    '''
    求两个最大公约数
    :param x: 数1
    :param y: 数2
    :return: 最大公约数
    '''
    (x,y)=(y,x) if x>y else(x,y)
    for factor in range(x,0,-1):
        if x % factor ==0 and y% factor ==0:
            return factor

print(ca(10,5))

def lcm(x,y):
    '''
    最大公倍数
    :param x: 
    :param y: 
    :return: 
    '''
    return x*y // ca(x,y)
print(lcm(32,48))