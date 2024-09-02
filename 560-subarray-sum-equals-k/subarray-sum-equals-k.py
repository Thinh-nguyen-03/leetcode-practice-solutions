class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cumulative_sum = {0: 1}
        current_sum = 0
        count = 0
        
        for num in nums:
            # Update the cumulative sum
            current_sum += num
            
            # Check if there is a previous sum that would give a subarray sum of k
            if current_sum - k in cumulative_sum:
                count += cumulative_sum[current_sum - k]
            
            # Update the cumulative sum frequency in the hash map
            if current_sum in cumulative_sum:
                cumulative_sum[current_sum] += 1
            else:
                cumulative_sum[current_sum] = 1
        
        return count