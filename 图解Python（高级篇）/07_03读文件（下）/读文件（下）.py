
"""
>>> file = open('myfile.txt')
>>> file.readline()
'1234567890\n'
>>> file.readline(7)
'abcdefg'
>>> file.readline(10)
'hijklmn\n'
>>> file.readline(3)
'opq'
>>> file.readline(-5)
'rstuvwxyz'
>>> file.close()



    
>>> file = open('myfile.txt')
>>> file.readlines()
['1234567890\n', 'abcdefghijklmn\n', 'opqrstuvwxyz']
>>> file.close()

>>> file = open('myfile.txt')
>>> file.readlines(8)
['1234567890\n']
>>> file.readlines(50)
['abcdefghijklmn\n', 'opqrstuvwxyz']
>>> file.close()
>>> file = open('myfile.txt')
>>> file.readlines(8)
['1234567890\n']
>>> file.readlines(-5)
['abcdefghijklmn\n', 'opqrstuvwxyz']
>>> file.close()    
"""


