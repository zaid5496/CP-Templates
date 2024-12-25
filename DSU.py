class DSU:
    def __init__(self, n):
        """Initialize DSU with n elements."""
        self.parent = list(range(n))  # Each element is its own parent initially
        self.size = [1] * n          # Size of each set is initially 1

    def make(self, v):
        """Initialize element v as its own set."""
        self.parent[v] = v
        self.size[v] = 1
    
    def get_size(self, v):
        """Get the size of the set containing element v."""
        parent = self.find(v)  # Find the root of v's set
        return self.size[parent]
        
    def find(self, v):
        """Find the root of the set containing v, with path compression."""
        if v == self.parent[v]:
            return v
        # Path compression: directly connect v to its root
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
 
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
 
    def connected(self, a, b):
        """Check if elements a and b are in the same set."""
        return self.find(a) == self.find(b)

# Example usage:
dsu = DSU(5)
dsu.union(0, 1)
dsu.union(1, 2)
print(dsu.connected(0, 2))  # True
print(dsu.get_size(0))      # 3
print(dsu.connected(3, 4))  # False
