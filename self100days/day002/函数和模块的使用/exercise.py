def is_prime(num):
    for i in range(2,num):
        if num%2==0:
            return False
    return True if num != 1 else False

print(is_prime(7))