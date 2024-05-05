class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    
        n = len(nums)

        concat = [0] * (2 * n)
        
        for i in range(n):
            concat[i] = concat[i + n] = nums[i]
        
        return concat