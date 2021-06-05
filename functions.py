# python for data science

# sequence data types

# functions

# STRING
strSample = 'python for ds'  

# in-built functions

print(strSample.capitalize()) # capitalize the first letter of first word

print(strSample.title()) # capitalize the first letter of each word

print(strSample.swapcase()) # swaps case from lower to upper and vice versa

print(strSample.find('f')) # get index position of particular character

print(strSample.index('f')) # get index position of particular character

print(strSample.count('o')) # count the number of times a particular character appears

print(strSample.replace('ds','data science')) # replaces a given portion of string with new one

print(strSample.isalnum())  # returns true if all characters are ASCII decimal or alphabetical else false

# string formatting

s1 = 'Malav'
s2 = 'Arunkumar'
s3 = 'Parikh'
full_name = '{} {} {}'.format(s1,s2,s3)
print(full_name)

# OR

fullName = f"{s1} {s2} {s3}"
print(fullName)

# all functions we can use on particular value

print(dir(full_name))

# find help on particular thing

#print(help(str)) # help on class string (str)
print(help(str.find))


# sequence datatype object initialization

listSample = [1,2,3,4.0,'sample']
tupleSample = (1,2,3,4.0,'sample')

from array import *
arrSample = array('i',[1,2,3,4,5])

dictSample = {1:'one','two':2,3:3,'four':'four'}

setSample = {'example',1,2,3,4.0}

rangeSample = range(1,12,2)


# length of the objects for different sequence datatype

print(f"string: {len(strSample)} \nlist: {len(listSample)} \ntuple: {len(tupleSample)}")
print(f"array: {len(arrSample)} \ndict: {len(dictSample)}\nset: {len(setSample)}\nrange: {len(rangeSample)}")

# reversing  a list
listSample.reverse()
print(listSample)
listSample.reverse()
print(listSample)


# removing all items from a sequence

# listSample.clear()
# dictSample.clear()
# setSample.clear()

# only works on list dict and set
# tuples cannot be cleared as they are immutable

# to clear tuple one way is to convert it to list and then clear it 
# and then agian convert it back to tuple

#########################################

# APPEND FUNCTION 
# it works only with array list and set

# array
print("Before: ", arrSample)
arrSample.append(10)
print("After: ", arrSample)
# list
# appending an element to list
print("Before: ", listSample)
listSample.append(10)
print("After: ", listSample)
# appending a iist to list
print("Before: ", listSample)
listSample.append([1,8])
print("After: ", listSample)

# set
print("Before: ", setSample)
setSample.add(10) # instead of append we have add function and it adds element at any position in the set
print("After: ", setSample)

# another function for adding elements to set is UPDATE

# update function takes only one argument
# it can be list, tuple, set or a dictionary
# it converts that argument to set and adds it to the existing set

setSample.update([89,78,67])
print(setSample)

setSample.update({108:'1','two':'2','three':'3'}) 
# if we pass a dictionary in update it takes the keys and adds it to the existing set
print(setSample) 

# DICTIONARY METHODS/FUNCTIONS

print(dictSample)

# adding element to dictionary
dictSample.update({'five':5})
print(dictSample)

# or
dictSample.update(six = 6)
print(dictSample)

# using update a new element can be added to the exisitng dictionary
# but if we try to add an element with the a duplicate key then it will
# either update it with new value or keep it as it is

dictSample.update(six = 6)
print(dictSample) # it remains same

dictSample.update(six = 'seven')
print(dictSample) # it is updated with new value 'seven'


print(list(dictSample)) # makes a list of the keys in dictionary

# length of dictionary
print(len(dictSample))

print(dictSample.get('six')) # get value at a particular key

print(dictSample.keys()) # returns list of keys in dictionary
print(dictSample.values()) # returns list of values in dictionary
print(dictSample.items()) # returns list of (key,value) tuples


### INSERT FUNCTION
# used to insert element at certain position
# can be used on list and arrays
# list
print("before: ",listSample)
listSample.insert(1,200) # element 200 added at 2nd position i.e index 1
print("after: ",listSample)
# array
print("before: ",arrSample)
arrSample.insert(1,200) # element 200 added at 2nd position i.e index 1
print("after: ",arrSample)

### POP FUNCTION
# it removes an element at given index from the object
# can be used on list, arrays, dict and set
# list
print("before: ",listSample)
listSample.pop(1) # remove element at position 1
print("after: ",listSample)
# array
print("before: ",arrSample)
arrSample.pop(1) # remove element at position 1
print("after: ",arrSample)
# set
print("before: ",setSample)
setSample.pop() # remove element at first position, no specific position can be given
print("after: ",setSample)
# dict
print("before: ",dictSample)
dictSample.pop('two') # removes element with the provided key, pop takes key as argument bcz dict is unordered
print("after: ",dictSample)

# if  nothing is passed to pop() in list and array it removes the last element by default
# list
print("before: ",listSample)
listSample.pop() # removes last element
print("after: ",listSample)
# array
print("before: ",arrSample)
arrSample.pop() # remove last element
print("after: ",arrSample)

print('*'*20)
### REMOVE FUNCTION
# it removes the given element
# can be used on list, arrays, dict and set
# list
print("before: ",listSample)
listSample.remove(4.0) # removes element 4.0
print("after: ",listSample)
# array
print("before: ",arrSample)
arrSample.remove(5) # removes element 10
print("after: ",arrSample)
# set
print("before: ",setSample)
setSample.remove('three') # remove element at first position, no specific position can be given
print("after: ",setSample)

# if mentioned element not present in set, remove method gives error
# using discard method, the set remains unchanged if the specified element is not present in set
print("before: ",setSample)
setSample.discard('example') # as example was removed earlier it returns the same set
print("after: ",setSample)

# DELETE FUNCTION
# delete any element at a position or entirely delete the sequence
# can also delete a range of sequence
print("before: ",listSample)
del listSample[-2]
print("after: ",listSample)


print('*'*20)
### ARRAY OPERATIONS

# EXTEND FUNCTION
# extends or adds to the end of array
print("before: ",arrSample)
arrSample.extend((789,909)) 
print("after: ",arrSample)

# difference between extend and append is that append is used if only one value is to be appended/added
# at the end of array. Using extend we can add more than one

# adding value from list to array
print("before: ",arrSample)
arrSample.fromlist(listSample)
print("after: ",arrSample)

# convert array into ordinary list
print(arrSample.tolist())
# doesnt permanently convert it but just that operation

#### SET OPERATIONS

A = {'sample',1,2,3,98,4.0,5.0}
B = {98,5.0, 100, 786}

print(A | B) # union operation
# or
print(A.union(B))

print(A & B) # intersection operation
# or
print(A.intersection(B))
