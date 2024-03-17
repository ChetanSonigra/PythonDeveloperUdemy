from pathlib import Path, PureWindowsPath
folder = Path('C:/Users/username/PycharmProjects/python1')  
# this works for any os. even if you remove C:, it will work.
file = folder/'Day6/test.txt'
my_file = open(file)
print(my_file.read())
my_file.close()
file = Path('C:/Users/username/PycharmProjects/python1/Day6/test.txt') 
windows_path = PureWindowsPath(file)
print(file.read_text(),file.name,file.suffix,file.stem,file.exists(),windows_path, sep='\n') 
    