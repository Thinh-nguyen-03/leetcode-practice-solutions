class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        unique_numbers = [num for num in freq if freq[num] == 1]

        if unique_numbers:
            return max(unique_numbers)
        else:
            return -1