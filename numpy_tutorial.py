# python for data science

# numpy

# import library

import numpy as np

# creating array with np

arraySample = np.array([1,2,3,4,5,6],dtype = int)
print(arraySample)

print(type(arraySample)) # data type of elements
print(len(arraySample)) # number of elements
print(arraySample.ndim) # dimension of array 
print(arraySample.shape) # size along each dimension specified as tuple/vector


# changing shape of the array

array2 = arraySample.reshape(3,2)
print(array2)

print(type(array2)) # data type of elements
print(len(array2)) # number of elements
print(array2.ndim) # dimension of array 
print(array2.shape) # size along each dimension specified as tuple/vector

# dimension is basically the number of indexes you would need to access that value
# like if I want to access 6 in the array2
print(array2[2][1]) # 3rd row i.e. index 2 and then inside that it is at column 2 i.e. index 1 so [2][1]

# here we know that there are 6 elements and we can reshape it as 3 rows and 2 columns
# what if we donot know the number of elements??

# we can keep any one of the argument as -1 and the other as a desired number of col or row
# -1 will automatically determine the number of columns best suited
array3 = arraySample.reshape(2,-1) # 2 rows and automatically determine 
print(array3)

print(array3.ndim)

# initializing numpy array for nested lists

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = [11,12,13,14,15]

np_array = np.array([list1,list2,list3])
print(np_array)

print(np_array.ndim)
print(np_array.shape)

# Numpy attributes

a1 = [1,2,3,4,5,6]

a = np.array(a1)
print(a)

# reshaping the array with shape
a.shape = (2,3)
print(a)

# array of evenly spaced numbers
a1 = np.arange(1,21,1) # takes in 3 arguments start, stop and skip
print(a1)

a2 = np.arange(14) # if only 1 argument given. it takes it as stop
# and the list starts from 0
print(a2)

# reshaping the array a1
new_a1 = a1.reshape(4,5)
print(new_a1)
print(new_a1.ndim)

# reshaping the array s2
new_a2 = a2.reshape(7,1,2) # 3 arguments = no. of vectors, rows, columns
print(new_a2)
print(new_a2.ndim)
print(new_a2[6][0][0])

print('#'*20)
# ARITHMETIC OPERATIONS

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x)
print(y)

# ADDITION IN ARRAYS
print(x+y)
print('#'*20)
print(np.add(x,y))

# SUBTRACTION IN ARRAYS
print(x-y)
print('#'*20)
print(np.subtract(x,y))

# MULTIPLICATION IN ARRAYS
print(x*y)
print('#'*20)
print(np.multiply(x,y))

# DIVISION IN ARRAYS
print(x/y)
print('#'*20)
print(np.divide(x,y))

# DOT PRODUCT IN ARRAYS
print(x.dot(y))
print('#'*20)
print(np.dot(x,y))


# NUMPY SUM

# sum of all elements in an array
sum1 = np.sum(x)
print(sum1)

# columnwise sum of elements in an array
sum_col = np.sum(x, axis=0) # axis = 0 -> column
print(sum_col)

# rowwise sum of elements in an array
sum_row = np.sum(x, axis=1) # axis = 1 -> row
print(sum_row)
