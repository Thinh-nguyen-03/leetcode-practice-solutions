class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(n):
            # Add the current element to the window
            current_sum += nums[right]
            
            # Shrink the window as much as possible while the sum is greater than or equal to the target
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        # If min_length is still infinite, that means no valid subarray was found
        return min_length if min_length != float('inf') else 0