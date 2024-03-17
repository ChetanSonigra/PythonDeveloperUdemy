import os, shutil, send2trash

print(os.getcwd())

file = open('python1\Day9\course.txt', 'w')
file.write('Test text')
file.close()

print(os.listdir('python1\Day9'))
shutil.move('python1\Day9\course.txt', 'python1\Day9\Example')

# os.unlink - deletes file in given path
# os.rmdir - deletes empty folder in given path
# shutil.rmtree - removes everythin recursively in given path

send2trash.send2trash('python1\Day9\Example')
# sends file to recyclebin

print(os.walk('python1'))
path = os.walk('python1\Day9')
for folder, subfolder, file in path:
    print('In folder: ', folder)
    print('sub folder are: ')
    for sub in subfolder:
        print(sub)
    print('Files are: ')
    for f in file:
        print(f)
    print('\n')