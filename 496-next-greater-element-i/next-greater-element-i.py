class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Hash map to store the next greater element for each number in nums2
        next_greater = {}
        # Stack to help find the next greater element
        stack = []
        
        # Traverse nums2 to fill the next_greater map
        for num in nums2:
            # While the stack is not empty and the current num is greater than the
            # element on top of the stack, it means we found the next greater element
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            
            # Push the current num to the stack
            stack.append(num)
        
        # For the remaining elements in the stack, no next greater element was found
        while stack:
            smaller_num = stack.pop()
            next_greater[smaller_num] = -1
        
        # Build the result for nums1 using the next_greater map
        result = []
        for num in nums1:
            result.append(next_greater[num])
        
        return result