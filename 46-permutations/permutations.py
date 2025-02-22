class Solution:
    def permute(self, nums):
        
        # Initialize the result list to store all permutations
        result = []
        
        # Define the backtracking function
        def backtrack(startIndex):
            
            # If the current permutation is complete, add it to the result
            if startIndex == len(nums):
                result.append(nums[:])
                return
            
            # Iterate over the possible numbers to place at the current position
            for i in range(startIndex, len(nums)):
                
                # Swap the current number with the startIndex number
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                
                # Recursively call backtrack for the next position
                backtrack(startIndex + 1)
                
                # Backtrack by swapping the numbers back
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
        
        # Start the backtracking process from the first index
        backtrack(0)
        
        # Return the list of all permutations
        return result