class DSURollback:
    def __init__(self, n):
        """Initialize DSU with n elements."""
        self.parent = list(range(n))  # Each element is its own parent initially.
        self.size = [1] * n           # Size of each set is initially 1.
        self.history = []             # Stack to record modifications.

    def find(self, v):
        """Find the representative (root) of the set containing v."""
        while v != self.parent[v]:
            v = self.parent[v]
        return v

    def union(self, a, b):
        """
        Union the sets containing elements a and b by size.
        Returns True if a union was performed; otherwise, returns False.
        """
        a = self.find(a)
        b = self.find(b)
        if a == b:
            # No union performed; record a dummy change for uniform rollback.
            self.history.append(None)
            return False
        
        # Ensure the larger set becomes the parent.
        if self.size[a] < self.size[b]:
            a, b = b, a
        
        # Record the change for rollback: (child, previous parent, parent, previous size).
        self.history.append((b, self.parent[b], a, self.size[a]))
        
        # Perform the union.
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def save(self):
        """
        Save the current state.
        Returns a checkpoint (the current history stack length) to which you can rollback later.
        """
        return len(self.history)

    def rollback(self, checkpoint):
        """
        Rollback to a given checkpoint.
        All union operations performed after the checkpoint are undone.
        """
        while len(self.history) > checkpoint:
            change = self.history.pop()
            if change is None:
                # A dummy change from a union that didn't modify the DSU.
                continue
            b, prev_parent, a, prev_size = change
            # Restore the DSU state.
            self.parent[b] = prev_parent
            self.size[a] = prev_size

    def connected(self, a, b):
        """Check if elements a and b are in the same set."""
        return self.find(a) == self.find(b)
