class Solution:
    def subsetsWithDup(self, nums):
        
        # Sort the input to handle duplicates
        nums.sort()
        
        # Initialize the result list
        result = []
        
        # Define the backtracking function
        def backtrack(start, path):
            
            # Append the current path to the result
            result.append(path[:])
            
            # Iterate over the possible next elements
            for i in range(start, len(nums)):
                
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] in the current path
                path.append(nums[i])
                
                # Recurse with the next starting index
                backtrack(i + 1, path)
                
                # Backtrack by removing the last element
                path.pop()
        
        # Start backtracking from the first index
        backtrack(0, [])
        
        # Return the result containing all unique subsets
        return result