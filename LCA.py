# https://codeforces.com/contest/1702/problem/G2

# change root if required

class LCA:
    def __init__(self, n):
        self.n = n
        self.LOG = (n).bit_length()
        self.depth = [0] * n
        self.ancestor = [[-1] * self.LOG for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, root=1):
        stack = [(root, -1)]  # (node, parent)
        self.depth[root] = 0

        while stack:
            v, p = stack.pop()
            self.ancestor[v][0] = p

            # fill ancestors for v
            for j in range(1, self.LOG):
                if self.ancestor[v][j-1] != -1:
                    self.ancestor[v][j] = self.ancestor[self.ancestor[v][j-1]][j-1]

            # push children
            for to in self.adj[v]:
                if to == p:
                    continue
                self.depth[to] = self.depth[v] + 1
                stack.append((to, v))

    def build(self, root=1):
        self.dfs(root)

    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        # Lift a up to same depth
        diff = self.depth[a] - self.depth[b]
        for j in range(self.LOG):
            if (diff >> j) & 1:
                a = self.ancestor[a][j]
        if a == b:
            return a
        # Lift both until just before LCA
        for j in reversed(range(self.LOG)):
            if self.ancestor[a][j] != self.ancestor[b][j]:
                a = self.ancestor[a][j]
                b = self.ancestor[b][j]
        return self.ancestor[a][0]

    def distance(self, a, b):
        l = self.lca(a, b)
        return self.depth[a] + self.depth[b] - 2 * self.depth[l]



'''''
n = int(input())
tree = LCA(n+1)

for i in range(n-1):
    u, v = inp()
    tree.add_edge(u, v)
    
tree.build(1)
'''''




































# import math

# class TreeAncestor:
#     def __init__(self, n, parent):
#         """
#         Initializes the TreeAncestor class with:
#         - n: The number of nodes in the tree.
#         - parent: An array where parent[i] is the parent of node i, or -1 if i is the root.
#         """
#         self.n = n
#         self.logn = int(math.ceil(math.log2(n))) + 1  # Maximum depth for binary lifting
#         self.ancestor = [[-1] * self.logn for _ in range(n)]  # Sparse table for 2^j-th ancestors
#         self.depth = [0] * n  # Depth of each node in the tree

#         # 1st ancestor (2^0)
#         for i in range(n):
#             self.ancestor[i][0] = parent[i]
#             if parent[i] != -1:
#                 self.depth[i] = self.depth[parent[i]] + 1  # Compute depth for each node

#         # Compute up to 2^logn ancestors using dp
#         for j in range(1, self.logn):
#             for i in range(n):
#                 if self.ancestor[i][j - 1] != -1:
#                     self.ancestor[i][j] = self.ancestor[self.ancestor[i][j - 1]][j - 1]

#     def get_kth_ancestor(self, node, k):
#         """
#         Finds the k-th ancestor of the given node.
#         - node: The starting node.
#         - k: The k-th ancestor to find.
#         Returns -1 if the k-th ancestor does not exist.
#         """
#         for i in range(self.logn):
#             if k & (1 << i):  
#                 node = self.ancestor[node][i]  
#                 if node == -1:  
#                     return -1
#         return node

#     def lca(self, u, v):
#         """
#         Finds the Lowest Common Ancestor (LCA) of nodes u and v.
#         - u: First node.
#         - v: Second node.
#         Returns the LCA of u and v.
#         """
#         if self.depth[u] < self.depth[v]:
#             u, v = v, u  # Ensure u is deeper

#         # Step 1: Bring u and v to the same depth
#         diff = self.depth[u] - self.depth[v]
#         u = self.get_kth_ancestor(u, diff)

#         if u == v:  # If they meet at the same node
#             return u

#         # Step 2: Binary lift both nodes until their ancestors match
#         for i in range(self.logn - 1, -1, -1):
#             if self.ancestor[u][i] != self.ancestor[v][i]:
#                 u = self.ancestor[u][i]
#                 v = self.ancestor[v][i]

#         # Step 3: The parent of u (or v) is the LCA
#         return self.ancestor[u][0]


# # Example Usage
# n = 7
# parent = [-1, 0, 0, 1, 1, 2, 2]  # Tree structure

# tree_ancestor = TreeAncestor(n, parent)

# # Query LCA
# print(tree_ancestor.lca(3, 4))  # Output: 1 (LCA of nodes 3 and 4 is 1)
# print(tree_ancestor.lca(5, 6))  # Output: 2 (LCA of nodes 5 and 6 is 2)
# print(tree_ancestor.lca(3, 6))  # Output: 0 (LCA of nodes 3 and 6 is 0)



