class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        frequency = {}
        for c in magazine:
            if c in frequency:
                frequency[c] += 1
            else:
                frequency[c] = 1
        for c in ransomNote:
            if c not in frequency or frequency[c] == 0:
                return False
            frequency[c] -= 1
        return True
