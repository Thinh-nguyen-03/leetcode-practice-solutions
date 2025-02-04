class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        max_freq = 0
        start = 0
        max_length = 0

        for end in range(len(s)):
            # Add the current character to the count
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            # Update the maximum frequency in the current window
            max_freq = max(max_freq, char_count[s[end]])
            
            # Check if the window is valid
            if (end - start + 1) - max_freq > k:
                # Shrink the window
                char_count[s[start]] -= 1
                start += 1
            
            # Update the maximum length of a valid window
            max_length = max(max_length, end - start + 1)
        
        return max_length
