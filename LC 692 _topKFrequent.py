from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
    
        count = Counter(words)
        return sorted(list(count.keys()), key = lambda x: (-count[x], x)) [:k]
