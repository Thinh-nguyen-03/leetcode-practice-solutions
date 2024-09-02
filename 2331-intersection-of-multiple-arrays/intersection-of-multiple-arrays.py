class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Start with the set of the first array
        intersection_set = set(nums[0])
        
        # Intersect with every other set
        for array in nums[1:]:
            intersection_set &= set(array)
        
        # Return the sorted list of the intersection set
        return sorted(intersection_set)