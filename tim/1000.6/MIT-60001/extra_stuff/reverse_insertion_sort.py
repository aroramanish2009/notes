def rev_insertion_sort(arr):
    # starts from index 1 with key value 2
    for i in range(1, len(arr)):
        key = arr[i]
        # j is index 0 based on next line for first loop
        j = i - 1
        #Only run this while loop if j is not negative and value of item at index j is less than key. This will be skipped if for element at 0 and 1 index in example below
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        #If the while loop is not true then this line makes no difference, if the while loop runs then this line assigns the value of key to index identified at loop termination. 
        arr[j + 1] = key

new_numbers = [ 5, 2, 8, 12, 1, 6]
rev_insertion_sort(new_numbers)
print(new_numbers)
