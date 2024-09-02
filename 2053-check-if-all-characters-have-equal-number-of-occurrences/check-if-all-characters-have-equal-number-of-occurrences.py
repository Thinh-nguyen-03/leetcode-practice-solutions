from collections import Counter

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Count the frequency of each character
        freq = Counter(s)
        
        # Get the set of unique frequency values
        unique_freq = set(freq.values())
        
        # If there's only one unique frequency, all characters have the same occurrence
        return len(unique_freq) == 1
        