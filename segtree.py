# 0-based indexing wala code he apna
# apne segtree me [l, r] dono included rehte he

class segtree:
    def __init__(self, arr):
        self.seg = [0]*(4*len(arr))
        self.n = len(arr)
        self.arr = arr
        
    def build_tree(self, i=0, low=0, high=None):    # low and high are the segments of the segtree
                                                         # desi bhasha me bole to upper bound aur lower bound
        if high is None:
            high = self.n - 1
            
        if low == high:                                  # ye condition hit hui mtlb ke root node(i - i wala) aa gya
            self.seg[i] = self.arr[low]
            return self.seg[i]                           # pachi ye value(i-i node ki value arr ka single element) ko return kar dia for further segment sum
        
        mid = (low + high)//2                            # nai to mid nikala left aur right subtree me dhundha
        left = self.build_tree(2*i + 1, low, mid)
        right = self.build_tree(2*i + 2, mid + 1, high)
        
        self.seg[i] =  left + right                      # segment sum
        
        return self.seg[i]                               # pachi ye value([low - high] node ki value (sum of arr[low:high + 1])) ko return kar dia for further segment sum
        
    def update(self, idx, val, i=0, low=0, high=None):      # i = index of the current node
        if high is None:
            high = self.n - 1
            
        if low == high:                                 # ith node shows the range sum from arr[low, high]
            self.seg[i] = val
            return 
        
        mid = (low + high)//2
        
        if idx <= mid:
            self.update(idx, val, 2*i + 1, low, mid)
        else:
            self.update(idx, val, 2*i + 2, mid + 1, high)
            
        self.seg[i] = self.seg[2*i + 1] + self.seg[2*i + 2]

    def query(self, l, r, i=0, low=0, high=None):
        if high is None:
            high = self.n - 1
        
        if r < low or l > high:         # no overlap
            return 0
        elif l <= low and high <= r:    # complete overlap      l...(low....high)...r
            return self.seg[i]
        else:
            mid = (low + high)//2
            
            left = self.query(l, r, 2*i + 1, low, mid)
            right = self.query(l, r, 2*i + 2, mid + 1, high)
            
            return left + right


# Input array
arr = [1, 2, 3, 4, 5]

# Initialize segment tree
tree = segtree(arr)

# Build the tree
tree.build_tree()

# Update index 2 to 10
tree.update(2, 10)

# Query range sum from index 1 to 3
print(tree.query(1, 3))  # Output: 16 (2 + 10 + 4)

# problems list:
# https://leetcode.com/problems/count-good-triplets-in-an-array/description/?envType=daily-question&envId=2025-04-15
