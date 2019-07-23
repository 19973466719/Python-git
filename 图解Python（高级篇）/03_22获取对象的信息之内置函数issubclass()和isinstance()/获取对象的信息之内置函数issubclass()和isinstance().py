
class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(A):
    pass

print(issubclass(D, A))    
print(issubclass(D, B))    

print(issubclass(D, (B, A, C)))     
print(issubclass(D, (B, C)))       

print(issubclass(bool, int))    
print(issubclass(bool, str))   

print(issubclass(bool, (str, int, dict)))
print(issubclass(bool, (str, list, dict)))   



print(isinstance(D(), D))   
print(isinstance(D(), A))  

print(isinstance(D(), (D, B, C)))   
print(isinstance(D(), (B, A, C)))   

