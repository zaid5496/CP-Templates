class FenwickTree:
    def __init__(self, n):
        # Initialize the Fenwick Tree with n elements
        # Internal array to store the tree values (1-indexed)
        self.tree = [0]*(n+5)       # extra buffer
        self.n = n + 2                  # to avoid index issues


    def update(self, index, delta):
        """Update the value at 'index' by 'delta'."""
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index  # Move to the next index to update

    def query(self, index):
        """Query the sum of values from 1 to 'index'."""
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index  # Move to the parent index
        return result

    def range_query(self, left, right):
        """Query the sum of values in the range [left, right]."""
        return self.query(right) - self.query(left - 1)

    def build(self, arr):
        """Build the Fenwick Tree from an array."""
        for i in range(1, len(arr) + 1):
            self.update(i, arr[i - 1])

# Example usage of Fenwick Tree
arr = [5, 3, 7, 2, 6]
n = len(arr)

fenwick = FenwickTree(n)

# Build the Fenwick Tree based on the array
fenwick.build(arr)

# Query the sum from 1 to 3
print(fenwick.query(3))  # Output will be 5 + 3 + 7 = 15

# Query the sum from 2 to 5
print(fenwick.range_query(2, 5))  # Output will be 3 + 7 + 2 + 6 = 18
