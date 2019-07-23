
with open('myfile.txt', 'r') as file:
    print(file.tell())  

with open('myfile.txt', 'a') as file:
    print(file.tell())  


with open('myfile.txt', 'r') as file:
    print(file.tell())  

    file.read(3)
    print(file.tell()) 

    file.read(4)
    print(file.tell())  

    file.read()
    print(file.tell())  

with open('myfile.txt', 'a') as file:
    print(file.tell())  # 10

    file.write('hello')
    print(file.tell())  # 15

with open('myfile.txt', 'w') as file:
    print(file.tell())  

    file.write('hello')
    print(file.tell()) 



import os

with open('myfile2.txt', 'rb') as file:
    print(file.tell())  

    # file.seek(3, os.SEEK_SET)
    # file.seek(3, 0)
    file.seek(3)
    print(file.tell())  

    file.seek(4, os.SEEK_CUR)
    print(file.tell())  

    file.seek(-2, os.SEEK_END)
    print(file.tell())  

with open('myfile2.txt', 'r+') as file:
    print(file.tell())  

    file.seek(3)
    print(file.tell())

    file.write('Python')
    print(file.tell())  