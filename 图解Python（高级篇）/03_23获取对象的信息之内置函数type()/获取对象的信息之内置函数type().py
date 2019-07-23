
class MyClass(object):
    pass

mc = MyClass()

print(type(mc))

print(type(18)) 

print(type('abc')) 



print(type(MyClass))  

print(type(int))        

print(type(str))      



def do_sth():
    pass

print(type(do_sth))

print(type(print))  



print(type(18) == int)      
print(type('abc') == str)   

# print(type(do_sth) == function)
# print(type(print) == builtin_function_or_method)

import types
print(type(do_sth) == types.FunctionType)   
print(type(print) == types.BuiltinFunctionType) 

