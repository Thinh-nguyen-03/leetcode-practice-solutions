from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_odd = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        result = 0
        
        for num in nums:
            if num % 2 == 1:
                count_odd += 1
            
            if count_odd - k in prefix_sums:
                result += prefix_sums[count_odd - k]
            
            prefix_sums[count_odd] += 1
        
        return result
