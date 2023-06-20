class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def char_to_index(self,ch):
        return ord(ch) - ord('a')
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        size = len(word)

        for l in range(size):
            ch = self.char_to_index(word[l])
            if not node.children[ch]:
                node.children[ch] = self.getNode()
            node = node.children[ch]
        
        node.isEndOfWord = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        size = len(word)

        for l in range(size):
            ch = self.char_to_index(word[l])
            if not node.children[ch]:
                return False
            node = node.children[ch]
        
        return node.isEndOfWord
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        node = self.root
        size = len(prefix)

        for l in range(size):
            ch = self.char_to_index(prefix[l])
            if not node.children[ch]:
                return False
            node = node.children[ch]
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
