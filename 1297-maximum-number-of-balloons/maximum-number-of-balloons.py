class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Count occurrences of all characters in the text
        count = Counter(text)
        
        # The word "balloon" requires:
        # 1 b, 1 a, 2 l's, 2 o's, 1 n
        b_count = count['b']
        a_count = count['a']
        l_count = count['l'] // 2
        o_count = count['o'] // 2
        n_count = count['n']
        
        # The maximum number of "balloon"s is determined by the minimum
        return min(b_count, a_count, l_count, o_count, n_count)
        