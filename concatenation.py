# python for data science

# sequence data types

# sequence concatenation

# STRING CONCATENATION

strSample = 'Learning'
# by using +
print(strSample + ' ' + 'Python') # + will join directly so need to specify ' ' (space) seperately
# by using ,
print(strSample,'Python') # only difference is that using , will automatically provide a space

# LIST CONCATENATION

listSample = [1,2,3,4.0,'Melb','Love']
print(listSample + ['Python',5,6.0])
# here comma cannot be used

# ARRAY CONCATENATION

from array import *
arraySample = array('i',[12,3,4,5])
print(arraySample + array('i',[9,8,7,6])) # array + array can be done
# print(arraySample + [9,8,7,6]) # array + list throws an error

# TUPLE CONCATENATION

tupSample = (1,2,3,4,5,'Monash')
print(tupSample + ('Python','DS'))

print(tupSample)
tupSample += ('Python','DS') # adding new tuples to existing ones
print(tupSample)