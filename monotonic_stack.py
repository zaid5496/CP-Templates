def prev_greater(arr):
    """Finds the Previous Greater Element (PGE) for each element in the array."""
    n = len(arr)
    result = [-1]*n  
    stack = []  

    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]                # change here to get the indices
        stack.append(i) 
    return result


def next_greater(arr):
    """Finds the Next Greater Element (NGE) for each element in the array."""
    n = len(arr)
    result = [-1] * n  
    stack = [] 
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]                    # change here to get the indices
        stack.append(i)  

    return result


# Example Usage:
arr = [10, 4, 2, 20, 40, 12, 30]

l = prev_greater(arr)  # l stores the previous greater element array
r = next_greater(arr)  # r stores the next greater element array

print("Array:", arr)
print("Previous Greater Elements:", l)
print("Next Greater Elements:", r)

# Array: [10, 4, 2, 20, 40, 12, 30]
# Previous Greater Elements: [-1, 10, 4, -1, -1, 40, 40]
# Next Greater Elements: [20, 20, 20, 40, -1, 30, -1]



x-----------------x-----------------x-----------------x-----------------x-----------------x-----------------x-----------------x-----------------x-----------------x

#=> monotonically decreasing stack



def next_smaller(arr):
    """Finds the Next Smaller Element (NSE) for each element in the array."""
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            index = stack.pop()
            result[index] = arr[i]  # Use 'i' for indices instead of value
        stack.append(i)

    return result


def prev_smaller(arr):
    """Finds the Previous Smaller Element (PSE) for each element in the array."""
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]  # Use stack[-1] for index or arr[stack[-1]] for value
        stack.append(i)

    return result


# Example usage
arr = [4, 5, 2, 10, 8]
print("Array:              ", arr)
print("Previous Smaller:   ", prev_smaller(arr))
print("Next Smaller:       ", next_smaller(arr))


# Array:               [4, 5, 2, 10, 8]
# Previous Smaller:    [-1, 4, -1, 2, 2]
# Next Smaller:        [2, 2, -1, 8, -1]
