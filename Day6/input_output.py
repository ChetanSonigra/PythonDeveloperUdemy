myfile = open('python1/Day6/test.txt')   # path can be relative to working directory not source code
print(myfile)

print(myfile.readline())  # gives one line from stricker with line breaks.
print(myfile.readline())
print(myfile.readlines())  # gives list of all lines from stricker.
print(myfile.read())       # gives all lines from stricker.

#All string methods can be used with lines, since they are string.

myfile.close()
myfile = open(r'C:\Users\username\PycharmProjects\python1\Day6\test.txt') #absolute path
# use r or double backslash(\\) to stop ignoring characters.
for l in myfile:
    print('Here it says: ' + l)
myfile.close()

# r - read only - default
# w - write only , overwrites
# a - append 
#
myfile = open('python1/Day6/test.txt','r')
#myfile.write('sdfs') - this will give error.
myfile.read()
myfile.close()

myfile = open('python1/Day6/test.txt','a')
myfile.write('sdfs')      # no seperator between 2 lines.
myfile.write('sasdsfd')
myfile.close()


myfile = open('python1/Day6/test.txt','w')
myfile.writelines(['Hloo','world','I am', 'here.'])
myfile.close()

