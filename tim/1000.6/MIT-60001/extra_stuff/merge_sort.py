'''
Merge Sort using recursion without memomization
Split into 2 functions:
divide: 
  - Splits List L recursively till it has 2 elements in it
  - Compare two elemets and merge using using merge function
merge:
  - Compare 2 Lists and merge them in sorted function
'''

import random
import time

largeunsorted_numbers = [random.randint(1, 100000) for _ in range(100000)]

def merge(left, right):
    #declare empty result list 
    result = []
    #declare i,j as 0 
    i,j = 0,0
    #Run until i,j are less than len of left,right list
    while i < len(left) and j < len(right):
        #if value at index i in left is less than index j in list right
        if left[ i ] < right[j]:
            #Append the smallest element to result list
            result.append(left[ i ])
            #Increment value of i by 1
            i += 1
        #If above is not true
        else:
            #Append the smallest element in Right list index j to result list
            result.append(right[j])
            #Increment j
            j += 1
    #If i is still smaller than len(left) then just append those values to result
    while (i < len(left)):
        result.append(left[ i ])
        i +=1
    #If j is still smaller than len(right) then just append those values to result
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result
    

def divide(LIST):
    #If only 1 element in list than return its value
    if len(LIST) < 2:
        return LIST[:]
    #Otherwise
    else:
        #calculate middle index value
        middle = len(LIST) // 2
        #divide List into smaller List using recursion
        left = divide(LIST[middle:])
        right = divide(LIST[:middle])
    #call merge function when smaller List are returned by divide
    return (merge(left, right))

numbers = [5,3,45,1,23,56,78,9,12,3]
print (divide(numbers))
start_time = time.time()
merge_sort_10k = divide(largeunsorted_numbers)
stop_time = time.time()
time_delta = stop_time - start_time
print ("Time to Merge Sort 100000 numbers:", time_delta )

