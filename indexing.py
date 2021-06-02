# python for data science

# sequence data types

# indexing

# access elements from index and get index i.e position of a value 

# String indexing

strSample = 'Machine'

# getting index for part of string
print(strSample.index('i'))
print(strSample.index('chi'))

# getting value at specific index position
print(strSample[3])
print(strSample[-3]) # -1 is the position of last value
#print(strSample[9]) # IndexError: string index out of range

print('-'*20)

# List indexing

listSample = [1,2,3,4,'Mach',5.0,'Lear']

# getting index for element of list
print(listSample.index('Mach'))
print(listSample.index(5.0))

# getting value at specific index position
print(listSample[-1]) # -1 is the position of last element in list
print(listSample[3]) 
#print(listSample[9]) # IndexError: List index out of range

print('-'*20)

# Array Indexing

from array import *

arraySample = array('i',[105,203,312,434,556,698,756,809])

for x in arraySample:
    print(x)

print(arraySample[2]) # element at index 2
print(arraySample.index(809)) # index position of value 809

print('-'*20)

# Tuple Indexing

tupleSample = (1,2,3,4,9.0,'RD','MP','champy')

print(tupleSample[-1]) # element at last index
print(tupleSample.index('RD')) # index position of value 'RD'

print('-'*20)

# Set Indexing

setSample = {1,2,3,4.0,'Sample','data','data', 24}
print(setSample)

#print(setSample[5]) 
# TypeError: set object is not subscriptable
# this error occurs as set is a non-sequential data. it cannot be indexed

print('-'*20)

# Dictionary Indexing

dictSample = {1:'one', 'two':2, 3:3, 'four':'four'}

#print(dictSample[2]) 
# error as there is no key 2 present
# dictionaries are indexed using keys
# they cannot be indexed by values

print(dictSample[1]) # to find value corresponding to key 1
print(dictSample['four']) # to find value corresponding to key 'four'

print('-'*20)

# Range indexing

rangeSample = range(1,13,2)

for x in rangeSample: 
    print(x)

print(rangeSample.index(3)) # index of value 3
print(rangeSample[3]) # value at index 3