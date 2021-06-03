# python for data science

# sequence data types

# sequence slicing

# STRING SLICING
strSample = 'Melbourne'
# 1st way
print(strSample[slice(1,7,2)]) # slice function takes in 3 arguments start, stop, skip
# 2nd way
print(strSample[1:7:2]) # here slicing without the function and directly give the values in [] with :
# reverse a string
print(strSample[::-1])

# LIST SLICING

listSample = [1,2,3.0,'Melb','MBIS']
print(listSample[2:]) # print all elements starting from 2nd index
print(listSample[:4]) # print all elements upto fourth index
print(listSample[:4:3]) # print elements from start upto fourth index but with skip or step 3
print(listSample[slice(0,4,3)])

# DICTIONARY AND SET

# both are non-sequential so slicing cannot be performed on them
# if done it will throw error

# ARRAY SLICING

from array import *

arraySample = array('i',[9,8,7,6,5])
print(arraySample[2:]) # print all elements starting from 2nd index