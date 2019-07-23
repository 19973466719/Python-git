
"""
>>> class MyClass(object):
...     pass
... 
>>> mc = MyClass()
>>> mc
<__main__.MyClass object at 0x103f41550>
>>> print(mc)
<__main__.MyClass object at 0x103f41550>
>>> str(mc)
'<__main__.MyClass object at 0x103f41550>'
>>> repr(mc)
'<__main__.MyClass object at 0x103f41550>'
"""

"""
>>> class MyClass(object):
...     def __str__(self):
...         return "__str__被调用"
... 
>>> mc = MyClass()
>>> mc
<__main__.MyClass object at 0x103e5c588>
>>> print(mc)
__str__被调用
>>> str(mc)
'__str__被调用'
>>> repr(mc)
'<__main__.MyClass object at 0x103e5c588>'
"""

"""
>>> class MyClass(object):
...     def __repr__(self):
...         return "__repr__被调用"
... 
>>> mc = MyClass()
>>> mc
__repr__被调用
>>> print(mc)
__repr__被调用
>>> str(mc)
'__repr__被调用'
>>> repr(mc)
'__repr__被调用'
"""

"""
>>> class MyClass(object):
...     def __str__(self):
...         return "__str__被调用"
...     def __repr__(self):
...         return "__repr__被调用"
... 
>>> mc = MyClass()
>>> mc
__repr__被调用
>>> print(mc)
__str__被调用
>>> str(mc)
'__str__被调用'
>>> repr(mc)
'__repr__被调用'
"""
