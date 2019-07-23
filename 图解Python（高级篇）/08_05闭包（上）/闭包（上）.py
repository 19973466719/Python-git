
def outer():
    a = 10
    def inner():
        print(a)
    return inner


def do_sth():
    temp = 8
    print(temp)

do_sth()
# print(temp)

outer_result = outer()
outer_result()  
outer()()       

print(outer_result.__closure__) 
print(outer_result.__closure__[0].cell_contents)    