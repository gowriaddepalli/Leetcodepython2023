class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        map = {}
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if map.get(sorted_string) is None:
                map[sorted_string] = [string]
            else:
                map[sorted_string].append(string)

        result = []
        for k,v in map.items():
            result.append(v)
        
        return result
