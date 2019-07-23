#判断一个数是不是回文数
def huiwen(num):
    temp=num
    total=0
    while temp>0:
        total=total*10+temp%10
        temp //= 10
        return total==num
num=int(input('num='))
print(huiwen(num))