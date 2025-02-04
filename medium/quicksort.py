def quick_sort(arr):
       # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element (here, the middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three sub-arrays
    left = [x for x in arr if x < pivot]    # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]   # Elements greater than the pivot
    
    # Recursively sort the left and right sub-arrays and concatenate the result
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [10, 23, 45, 70, 11, 15]
sorted_arr = quick_sort(arr)

print(f"Sorted array: {sorted_arr}")
