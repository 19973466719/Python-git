def factorial(num):
    '''
    求阶乘
    :param num:非负整数 
    :return: num的阶乘
    '''
    result=1
    for n in range(1,num+1):
        result *=n
        return result
m=int(input('m='))
n=int(input('n='))
print(factorial(m)//factorial(n)//factorial(m-n))