 class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
        self.countLetter = 0
        self.countWord = 0

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
            node.countLetter += 1
        
        node.isEndOfWord = True
        node.countWord += 1
        

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node = self.root
        size = len(word)

        for l in range(size):
            ch = self.char_to_index(word[l])
            if not node.children[ch]:
                return 0
            node = node.children[ch]
        
        return node.countWord
        

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """

        node = self.root
        size = len(prefix)

        for l in range(size):
            ch = self.char_to_index(prefix[l])
            if not node.children[ch]:
                return 0
            node = node.children[ch]

        return node.countLetter

        

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        size = len(word)

        for l in range(size):
            ch = self.char_to_index(word[l])
            node = node.children[ch]
            node.countLetter -= 1
        
        node.countWord -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
