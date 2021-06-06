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

