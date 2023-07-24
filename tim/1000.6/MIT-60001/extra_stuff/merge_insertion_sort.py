'''
Merge Sort + insertion sort when size of List is smaller 
'''
import random
import time

largeunsorted_numbers = [random.randint(1, 100000) for _ in range(100000)]

def insertion_sort(arr):
    # Start loop from second element to last element.
    for i in range(1, len(arr)):
        # Assign value of key equal to loop itration
        key = arr[i]  # Current element to be inserted
        # assign j value of 1 less than iteration i
        j = i - 1  # Index of the element to the left of the current element

        # Move elements of arr[0..i-1], that are greater than the key,
        # to one position ahead of their current position
        # Only kicks in if j is greater than 0 and index position j's value is more than key
        while j >= 0 and arr[j] > key:
            # swap value of i index position with j index position since its greater
            arr[j + 1] = arr[j]
            # reduce the j index by to keep while loop in maintenance
            j -= 1
        # This is part of for loop and will assign key value to place vacated by replaced j index.
        arr[j + 1] = key  # Insert the key into its correct position
    return arr

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
    #If only 5 element in list than Insert sort and return 
    if len(LIST) < 6:
        LIST = insertion_sort(LIST)
        return LIST
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
