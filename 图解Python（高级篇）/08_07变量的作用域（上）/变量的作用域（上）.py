
def do_sth(a):
    print(a)
    b = 3
    print(b)

do_sth(2)
# print(a)    
# print(b)    


def outer():
    m = 5
    def inner():
        print(m)
    inner()

outer()
# print(m)   


# print(g)   
g = 18
