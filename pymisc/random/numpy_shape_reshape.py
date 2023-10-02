'''
The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
[[1 2]
[3 4]
[5 6]]
The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]
'''

import numpy
myarray = numpy.array(list(map(int,input().split(" "))))
myarray.shape = (3,3)
print (myarray)

