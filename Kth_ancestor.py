import math

class TreeAncestor:
    def __init__(self, n, parent):
        """
        Initializes the TreeAncestor class with:
        - n: The number of nodes in the tree.
        - parent: An array where parent[i] is the parent of node i, or -1 if i is the root.
        """
        self.n = n
        self.logn = int(math.ceil(math.log2(n))) + 1            # Maximum depth for binary lifting ya fir width of the sparse table
        self.ancestor = [[-1] * self.logn for _ in range(n)]    # Sparse table for 2^j-th ancestors

        # 1st ancestor (2^0)
        for i in range(n):
            self.ancestor[i][0] = parent[i]

        #dp use karke calculate upto 2^logn ancestors
        for j in range(1, self.logn):
            for i in range(n):
                if self.ancestor[i][j - 1] != -1:       # agar aisa he to baap iska possible ich nai he
                    self.ancestor[i][j] = self.ancestor[self.ancestor[i][j - 1]][j - 1]  # purvaj ka purvaj(chad)

    def get_kth_ancestor(self, node, k):
        """
        Finds the k-th ancestor of the given node.
        - node: The starting node.
        - k: The k-th ancestor to find.
        Returns -1 if the k-th ancestor does not exist.
        """
        for i in range(self.logn):  
            if k & (1 << i):                    # check kar rahe he ki ith bit set he ke nai
                node = self.ancestor[node][i]   # agar he to curr_node ka 2^ith parent current node ban jayinga
                if node == -1:                  # agar baap -1 ho gya to rukja bhidu, tham ja aur -1 return kar de
                    return -1
        return node



# Initialize TreeAncestor with `n` nodes and their parent relationships
n = 7
parent = [-1, 0, 0, 1, 1, 2, 2]  # Tree structure
tree_ancestor = TreeAncestor(n, parent)

# Query the k-th ancestor of a node
print(tree_ancestor.get_kth_ancestor(3, 1))  # Output: 1 (1st ancestor of node 3)
print(tree_ancestor.get_kth_ancestor(5, 2))  # Output: 0 (2nd ancestor of node 5)
print(tree_ancestor.get_kth_ancestor(6, 3))  # Output: -1 (3rd ancestor doesn't exist)
