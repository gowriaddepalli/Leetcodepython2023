
# Online Python - IDE, Editor, Compiler, Interpreter

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        
class Trie:
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()
    
    def char_to_Index(self, char):
        return ord(char) - ord('a')
    
    def insert(self, key):
        node = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_Index(key[level])
            
            if not node.children[index]:
                node.children[index] = self.getNode()
            node = node.children[index]
                
        node.isEndOfWord = True
    
    def search(self, key):
        node = self.root
        length = len(key)
        
        for level in range(length):
            index = self.char_to_Index(key[level])
            
            if not node.children[index]:
                return False
            else:
                node = node.children[index]
        
        return node.isEndOfWord


def main():
    
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    op = ["trr", "plpl"]
            
    print(keys) 
    
    t = Trie()
    
    for key in keys:
        t.insert(key)
    
    for key in keys:
        print(t.search(key))
        
    for key in op:
        print(t.search(key))
    
    #print(t.root.children)
    
    
    
    
main()
    
