
class MyClass(object):
    def __str__(self):
        return "xxx"

    __repr__ = __str__


"""
>>> str("Hello,\nworld!")
'Hello,\nworld!'
>>> repr("Hello,\nworld!")
"'Hello,\\nworld!'"
"""