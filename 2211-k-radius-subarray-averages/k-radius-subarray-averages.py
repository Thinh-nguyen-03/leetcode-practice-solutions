class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1] * n
        
        window_size = 2 * k + 1

        if n < window_size:
            return result
        
        window_sum = sum(nums[:window_size])
        
        for i in range(k, n - k):
            # Compute the average of the window centered at index i
            result[i] = window_sum // window_size
            
            # Move the window to the right: subtract the leftmost element and add the next element
            if i + k + 1 < n:
                window_sum += nums[i + k + 1] - nums[i - k]
        
        return result