class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        start = 0

        for end in range(len(s)):
            # Shrink the window until the character is unique
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            # Add the new character to the set
            char_set.add(s[end])
            # Update the maximum length
            max_length = max(max_length, end - start + 1)

        return max_length