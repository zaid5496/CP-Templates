import math

class TreeAncestor:
    def __init__(self, n, parent):
        """
        Initializes the TreeAncestor class with:
        - n: The number of nodes in the tree.
        - parent: An array where parent[i] is the parent of node i, or -1 if i is the root.
        """
        self.n = n
        self.logn = int(math.ceil(math.log2(n))) + 1  # Maximum depth for binary lifting
        self.ancestor = [[-1] * self.logn for _ in range(n)]  # Sparse table for 2^j-th ancestors
        self.depth = [0] * n  # Depth of each node in the tree

        # 1st ancestor (2^0)
        for i in range(n):
            self.ancestor[i][0] = parent[i]
            if parent[i] != -1:
                self.depth[i] = self.depth[parent[i]] + 1  # Compute depth for each node

        # Compute up to 2^logn ancestors using dp
        for j in range(1, self.logn):
            for i in range(n):
                if self.ancestor[i][j - 1] != -1:
                    self.ancestor[i][j] = self.ancestor[self.ancestor[i][j - 1]][j - 1]

    def get_kth_ancestor(self, node, k):
        """
        Finds the k-th ancestor of the given node.
        - node: The starting node.
        - k: The k-th ancestor to find.
        Returns -1 if the k-th ancestor does not exist.
        """
        for i in range(self.logn):
            if k & (1 << i):  
                node = self.ancestor[node][i]  
                if node == -1:  
                    return -1
        return node

    def lca(self, u, v):
        """
        Finds the Lowest Common Ancestor (LCA) of nodes u and v.
        - u: First node.
        - v: Second node.
        Returns the LCA of u and v.
        """
        if self.depth[u] < self.depth[v]:
            u, v = v, u  # Ensure u is deeper

        # Step 1: Bring u and v to the same depth
        diff = self.depth[u] - self.depth[v]
        u = self.get_kth_ancestor(u, diff)

        if u == v:  # If they meet at the same node
            return u

        # Step 2: Binary lift both nodes until their ancestors match
        for i in range(self.logn - 1, -1, -1):
            if self.ancestor[u][i] != self.ancestor[v][i]:
                u = self.ancestor[u][i]
                v = self.ancestor[v][i]

        # Step 3: The parent of u (or v) is the LCA
        return self.ancestor[u][0]


# Example Usage
n = 7
parent = [-1, 0, 0, 1, 1, 2, 2]  # Tree structure

tree_ancestor = TreeAncestor(n, parent)

# Query LCA
print(tree_ancestor.lca(3, 4))  # Output: 1 (LCA of nodes 3 and 4 is 1)
print(tree_ancestor.lca(5, 6))  # Output: 2 (LCA of nodes 5 and 6 is 2)
print(tree_ancestor.lca(3, 6))  # Output: 0 (LCA of nodes 3 and 6 is 0)
