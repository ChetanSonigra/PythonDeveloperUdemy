import zipfile

my_zip = zipfile.ZipFile('python1/Day9/file_compressed.zip', 'w')

my_zip.write('python1/Day9/a.txt', 'a.txt')
my_zip.write('python1/Day9/c.txt','c.txt')

my_zip.close()

# delete files a.txt , c.txt in folder.

open_zip = zipfile.ZipFile('python1/Day9/file_compressed.zip', 'r')
open_zip.extractall('python1/Day9/')


# shutil module

import shutil

source_folder = 'python1/Day9/Example'
destination_file = 'shutil_compressed'
shutil.make_archive(destination_file, 'zip', source_folder)

shutil.unpack_archive('shutil_compressed.zip', 'python1/Day9/shutil_extract', 'zip')


shutil.unpack_archive('C:/Users/username/Downloads/jpegsrc.v9.tar.gz', 'C:/Users/username/AppData/Roaming/Python/Python311/site-packages/jpeglib', 'tar')