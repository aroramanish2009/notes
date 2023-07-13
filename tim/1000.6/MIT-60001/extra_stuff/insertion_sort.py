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

# Example usage
numbers = [5, 2, 8, 12, 1, 6]
insertion_sort(numbers)
print(numbers)
