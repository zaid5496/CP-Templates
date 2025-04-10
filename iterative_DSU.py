# https://codeforces.com/problemset/problem/1213/G

class DSU:
    def __init__(self, n):
        """Initialize DSU with n elements."""
        self.parent = list(range(n))  # Each element is its own parent initially
        self.size = [1] * n          # Size of each set is initially 1
        self.components = n

    def make(self, v):
        """Initialize element v as its own set."""
        self.parent[v] = v
        self.size[v] = 1
    
    def get_size(self, v):
        """Get the size of the set containing element v."""
        parent = self.find(v)
        return self.size[parent]
        
    def find(self, v):
        """Iteratively find the root of the set containing v, with path compression."""
        root = v
        # First, find the root
        while root != self.parent[root]:
            root = self.parent[root]
        
        # Then, path compression
        while v != root:
            next_v = self.parent[v]
            self.parent[v] = root
            v = next_v
        
        return root
 
    def union(self, a, b):
        """Union the sets containing elements a and b by size."""
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA != rootB:
            # Attach smaller tree under larger tree
            if self.size[rootA] < self.size[rootB]:
                rootA, rootB = rootB, rootA
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
            self.components -= 1
    
    def get_components(self):
        """returns the number of connected components"""
        return self.components - 1  # - 1 bcs 1 of 0 indexing
        
    def connected(self, a, b):
        """Check if elements a and b are in the same set."""
        return self.find(a) == self.find(b)
