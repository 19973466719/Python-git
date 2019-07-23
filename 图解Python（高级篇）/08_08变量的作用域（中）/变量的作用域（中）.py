
print(id(123))
id = "Global"

def outside():
    id = "Enclosing"
    def inside():
        id = "Local"
        print(id)
    inside()

outside()


i = 11
def fun1():
    i = 22
    print(i)
fun1()      
print(i)    


j = 0
def fun2():
    # print(j) 
    j = 5
fun2()
