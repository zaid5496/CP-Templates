
def prev_greater(arr):
    """Finds the Previous Greater Element (PGE) for each element in the array."""
    n = len(arr)
    result = [-1]*n  
    stack = []  

    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
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
            result[index] = arr[i]
        stack.append(i)  

    return result


# Example Usage:
arr = [10, 4, 2, 20, 40, 12, 30]

l = prev_greater(arr)  # l stores the previous greater element array
r = next_greater(arr)  # r stores the next greater element array

print("Array:", arr)
print("Previous Greater Elements:", l)
print("Next Greater Elements:", r)
