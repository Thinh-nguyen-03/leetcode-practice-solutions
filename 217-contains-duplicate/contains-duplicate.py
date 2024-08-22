class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        appeared = {}
        
        for num in nums:
            
            if num in appeared:
                return True
            else:
                appeared[num] = 1

        return False 
        
        