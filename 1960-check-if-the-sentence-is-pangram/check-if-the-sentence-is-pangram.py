class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        seen = [False] * 26

        for curr_char in sentence:
            seen[ord(curr_char) - ord('a')] = True
        
        for status in seen:
            if not status:
                return False
        return True