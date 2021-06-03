# python for data science

# sequence data types

# sequence multiplication

# object * integer

# STRING
strSample = 'python'
print(strSample*3)

# LIST
listSample = [1,2,3,4.0,'Melb']
print(listSample*2) # concatenates the whole list to the original one
# but if done on one element individually
print(listSample[3]*2) # it multiplies the value specified if it is integer or float
# if it is a string it concatenates it as it is after the original string

# replace a particular value by multiplying it with 2 in original list
print(listSample) # before
listSample[3] *= 2
print(listSample) # after

# TUPLE

tupSample = (1,2,3,4.0,'Melb')
print(tupSample[3]*2) # multiplies a given element 
print(tupSample[4]*2) # multiplies a given element 

# if multiplied with whole tuple, it gets doubles
tupSample *= 2
print(tupSample)

# a single element can be multiplied with another sperately
# but like lists a single element cannot be multiplied and replaced in the original tuple
tupSample[3] * 2 # this is allowed
# print(tupSample) # gives error 

# ARRAY

# similar to other one it is repeated again
from array import *
arraySample = array('i',[1,2,3,4,5])
print(arraySample*2)

# RANGE
# in range this will not work