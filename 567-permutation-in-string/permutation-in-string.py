class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency count for s1
        count1 = [0] * 26
        for char in s1:
            count1[ord(char) - ord('a')] += 1

        # Frequency count for the first window in s2
        count2 = [0] * 26
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        # Compare count1 and count2 in the sliding window
        for i in range(len(s2) - len(s1)):
            if count1 == count2:
                return True
            # Slide the window: remove the leftmost character and add the next character
            count2[ord(s2[i]) - ord('a')] -= 1
            count2[ord(s2[i + len(s1)]) - ord('a')] += 1

        # Check the last window
        return count1 == count2
