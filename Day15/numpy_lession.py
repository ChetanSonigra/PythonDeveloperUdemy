import numpy as np # numerical python
# we can create a one-dimentional array with a funtion np.array()

# documentation
# https://numpy.org/doc/1.24/
array_1d = np.array([1,2,3,4,5])

# or 2D array
array_2d = np.array([[1,2,3],
                     [4,5,6]])

# or 3D array
array_3d = np.array([[[1,2,3],
                     [4,5,6],
                      [4,4,4]],
                     [[7,8,9],
                      [10,11,12],
                      [4,4,4]]])

# Attributes of one,two and three dimentional array (shape, number of dimention, datatype,size,type)
print(array_1d.shape, array_1d.ndim, array_1d.dtype, array_1d.size, type(array_1d), sep = ', ')
print(array_2d.shape, array_2d.ndim, array_2d.dtype, array_2d.size, type(array_2d), sep = ', ')
print(array_3d.shape, array_3d.ndim, array_3d.dtype, array_3d.size, type(array_3d), sep = ', ')

# we import pandas as pd and create a datafram from 2d array
import pandas as pd
data = pd.DataFrame(array_2d)
print(data)

# create an array of size 4x3 with only ones(1)
ones = np.ones((4,3))
print(ones, ones.dtype)

# we create an array of size 2,4,3 consisting only of zeroes(0)
zeros = np.zeros((2,4,3))
print(zeros, zeros.dtype)

# we create an array of numbers ranging from 0 to 100 jumping from 5 to 5
array_1 = np.arange(0,100,5)
print(array_1)

# we create an array of random integer numbers between 0 to 10 of size (2,5)\
array_2 = np.random.randint(0,10,(2,5))
print(array_2)

# we create an array of random decimal numbers between 0 and 1 of size (3,5)
array_3 = np.random.random((3,5))
print(array_3)

# we set the seed of random numbers at 27
np.random.seed(27)

# we create an array of random integer numbers between 0 to 10 of size (3,5)\
array_4 = np.random.randint(0,10,(3,5))
print(array_4)

# we find unique values of array_4
print(np.unique(array_4))

# we extract the element at index 1 from array_4
print(array_4[1])
# we extract the first 2 rows from array_4
print(array_4[:2])
# we extract the first 2 items of first 2 rows.
print(array_4[:2, :2])

# we create 2 arrays of size 3x4. one with random numbers from 0 to 10 and other with ones.
array_5 = np.random.randint(0,10,(3,4))
array_6 = np.ones((3,4))

# display array_5 and array_6
print(array_5, array_6, sep='\n')

print(array_5 + array_6)

# we now create an array of size 4x3 with ones
array_7 = np.ones((4,3))

# we will try to add array_6(3,4) and array_7(4,3)
# print(array_6 + array_7)  -- can't add array with different size

# we will create another array with size 4x3 with ones
array_8 = np.ones((4,3))
# substract array_7 from array_8
print(array_8- array_7)

# we create 2 arrays of size 3,3 with random numbers form 0 to 5
array_9 = np.random.randint(0,5,(3,3))
array_10= np.random.randint(0,5,(3,3))
print(array_9, array_10, sep='\n')

# multiply array_9 with array_10
print(array_9* array_10)

# square the array_9
print(array_9**2)

# sqrt of array_10
print(np.sqrt(array_10))

# min, max, avg of array_9
print(array_9.min(), array_9.max(), array_9.mean())

# we change the shape of array_9 from 3x3 to 9x1 and store it in array_11
array_11 = array_9.reshape((9,1))
print(array_11)

# we transpose the array_11
print(array_11.transpose(), array_11.T, sep= '\n')

# we compare array_9 and array_10 to know which elements of array_9 are greater than those of array_10
array_12 = array_9 > array_10
print(array_12)

print(array_9<= array_10)

print(array_9 >2)

# sorting the elements of array_9
print(array_9, np.sort(array_9), sep = '\n')


