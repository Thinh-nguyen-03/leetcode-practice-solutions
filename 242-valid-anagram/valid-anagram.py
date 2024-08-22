class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char in count:
                count[char] -= 1
                if count[char] < 0:
                    return False
            else:
                return False
        
        return all(value == 0 for value in count.values())
        