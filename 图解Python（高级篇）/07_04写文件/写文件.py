
"""
>>> file = open('myfile.txt', 'w')
>>> file.write('hello')
5
>>> file.write('python')
6
>>> file.flush()
>>> file.close() 
>>> file = open('myfile.txt', 'a')
>>> file.write('hello')
5
>>> file.write('python')
6
>>> file.close()



>>> file = open('myfile.txt', 'w')
>>> file.writelines(['123\n', '456\n', '789'])
>>> file.close()
"""



