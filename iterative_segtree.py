class IterativeSegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: a + b):
        """
        Initializes the segment tree.
        :param data: The list of elements to build the tree from.
        :param default: The default value (e.g., 0 for sum, float('inf') for min).
        :param func: The associative function used for queries.
        """
        self.n = len(data)
        self.default = default
        self.func = func
        # Next power of two greater than or equal to n
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        
        # Build the tree as an array of length 2 * size.
        self.tree = [default] * (2 * self.size)
        # Initialize leaves.
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # Build the tree by calculating parents.
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, index, value):
        """
        Updates the value at index and rebuilds the tree accordingly.
        :param index: The index in the original array to update.
        :param value: The new value.
        """
        # Set value at leaf node.
        i = self.size + index
        self.tree[i] = value
        
        # Update ancestors.
        while i > 1:
            i //= 2
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    
    def query(self, l, r):
        """
        Queries the range [l, r) (l inclusive, r exclusive).
        :param l: Left index (inclusive).
        :param r: Right index (exclusive).
        :return: The result of combining the values in the interval.
        """
        res_left = self.default
        res_right = self.default
        
        # Shift indices to the leaves.
        l += self.size
        r += self.size
        
        while l < r:
            if l % 2 == 1:
                res_left = self.func(res_left, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res_right = self.func(self.tree[r], res_right)
            l //= 2
            r //= 2
        
        return self.func(res_left, res_right)

# Example usage:
if __name__ == "__main__":
    # Initialize data and create the segment tree for range-sum queries.
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = IterativeSegmentTree(data, default=0, func=lambda a, b: a + b)
    
    # Query the sum of the interval [1, 5) => 3 + 5 + 7 + 9 = 24
    print("Range Sum [1, 5):", seg_tree.query(1, 5))
    
    # Update index 3 to 10.
    seg_tree.update(3, 10)
    
    # Now query again.
    print("Range Sum [1, 5) after update:", seg_tree.query(1, 5))
