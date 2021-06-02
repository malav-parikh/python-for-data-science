# python for data science

# sequence data types

# sequence object initialization

# STRING
strSample = 'Malav'
print(strSample)
# strings are immutable i.e. they cannot be changed or altered

# LISTS

lstNumbers = [1,2,3,3,3,4,5,6]
print(lstNumbers)
# this is a list containing only numbers basically a single data type
# another property of list is that it can contain duplicates

lstSample = [1,'Malav',3.0,True,'Hi']
print(lstSample)
# this is a list containing mixed data type
# lists can contain elements of different data types
# lists are mutable i.e they can be changed or altered even after their creation

# ARRAYS
# to use array in python we need to import from array module
# then to define an array we need to pass data type and values in array function
# like array('data-type',[value1, value2,...])

from array import *
arraySample = array('i',[1,2,3,4])

# printing an array
for i in arraySample:
    print(i)


# TUPLES

tupeSample = (1,2,3,3,5,'a',3.0,'b')
print(tupeSample)
# tuples are like list, they can have elements of different data types
# they are stored in paranthesis () 
# they are immutable

tupleSample = 1, 2, 'packing'
print(tupleSample)
# tuples can be written without paranthesis as well
# this is called tuple packing

# DICTIONARY

dictSample = {'1':'one',2:'two', 3.0:'three','four':True}
print(dictSample)
# dictionary holds key value pairs in between {}
# the keys and values can be of any data type but
# the keys should be unique i.e, they cannot be repeated

# creating dictionary using dict function
# the only difference is that the key value pairs are passed as tuples in a list
dictSample2 = dict([('1','one'),(2,'two'),(3.0,'three'),('four',True)])
print(dictSample2)

# SET

setSample = {'sample',1,2,3,4.0,True,3,4.0,True}
print(setSample)
# a set is also like list where it can hold elements of different data types
# the difference is that it cannot hold another list or set inside it
# the elements are passed between {}
# sets cannot contain duplicates
# printing the above example will not print the repeated values only once

setSample2 = set([1,2,3,4,5])
print(setSample2)
# creating set using set function

# another way for creating set
setExample = set('example')
print(setExample)

# RANGE
# for creating a sequence of integers
# useful in for loop
# takes in 3arguments (start, end, skip or step)
# if end is 51 considers only upto 50 i.e n-1

rangeSample = range(0,51,10)
print(rangeSample)

for x in rangeSample:
    print(x)

