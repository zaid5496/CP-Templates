class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ptr = self.root
        for x in word:
            idx = ord(x) - ord('a')
            if not ptr.child[idx]:
                ptr.child[idx] = TrieNode()
            ptr = ptr.child[idx]
        ptr.isEndOfWord = True        

    def search(self, word):
        ptr = self.root
        for x in word:
            idx = ord(x) - ord('a')
            if not ptr.child[idx]:
                return False
            ptr = ptr.child[idx]
        return ptr.isEndOfWord

    def startsWith(self, prefix):
        ptr = self.root
        for x in prefix:
            idx = ord(x) - ord('a')
            if not ptr.child[idx]:
                return False
            ptr = ptr.child[idx]
        return True

#(Z)--(A)--(I)--(D)--(isEndOfWord=True)




# Sample usage and debugging
trie = Trie()

# Insert words into the Trie
trie.insert("apple")
trie.insert("app")

# Search for a word
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("appl"))   # Output: False
print(trie.search("banana")) # Output: False

# Search for a prefix
print(trie.startsWith("app")) # Output: True
print(trie.startsWith("ban")) # Output: False
print(trie.startsWith("ap"))  # Output: True
