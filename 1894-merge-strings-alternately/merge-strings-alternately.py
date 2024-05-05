class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = []
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        
        result.extend(word1[min_len:])
        result.extend(word2[min_len:])
        
        return ''.join(result)