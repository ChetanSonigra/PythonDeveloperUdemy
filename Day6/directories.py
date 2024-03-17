# path and os modules are important.

import os
path = os.getcwd()
print(path)
os.chdir('C:\\Users\\username')
path = os.getcwd()
print(path)
os.chdir('C:\\Users\\username\\PycharmProjects')
os.makedirs('C:\\Users\\username\\PycharmProjects\\example')
path = os.getcwd()
print(path)

path = "C:\\Users\\username\\PycharmProjects\\Day6\\test.txt"
a = os.path.basename(path);print(a)   # gives specific file/dir name
a = os.path.dirname(path);print(a)    # current immidiate parent dir
a = os.path.split(path);print(a)      # splits path
path = "C:\\Users\\username\\PycharmProjects\\Day6\\"
a = os.path.basename(path);print(a)   # gives specific file/dir name
a = os.path.dirname(path);print(a)    # current immidiate parent dir
a = os.path.split(path);print(a)      # splits path
path = "C:\\Users\\username\\PycharmProjects\\Day6"
a = os.path.basename(path);print(a)   # gives specific file/dir name
a = os.path.dirname(path);print(a)    # current immidiate parent dir
a = os.path.split(path);print(a)      # splits path

os.rmdir('C:\\Users\\username\\PycharmProjects\\example')

from pathlib import Path
folder = Path('C:/Users/username/PycharmProjects/python1')  
# this works for any os. even if you remove C:, it will work.
file = folder/'Day6/test.txt'
my_file = open(file)
print(my_file.read())
my_file.close()
