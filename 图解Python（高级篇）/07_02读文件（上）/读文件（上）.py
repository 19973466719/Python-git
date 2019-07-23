
"""
>>> import io
>>> io.DEFAULT_BUFFER_SIZE
8192    

>>> file = open('myfile.txt')
>>> file.read()
'1234567890\nabcdefghijklmn\nopqrstuvwxyz'
>>> file.close()  

>>> file = open('myfile.txt')
>>> file.read(12)
'1234567890\na'
>>> file.read(30)
'bcdefghijklmn\nopqrstuvwxyz'
>>> file.close()

>>> file = open('myfile.txt')
>>> file.read(12)
'1234567890\na'
>>> file.read(-5)
'bcdefghijklmn\nopqrstuvwxyz'
>>> file.close()
"""

