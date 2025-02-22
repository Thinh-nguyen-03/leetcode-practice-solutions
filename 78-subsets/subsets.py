class Solution:
    def subsets(self, nums):
        
        # Initialize the result list to store all subsets
        result = []
        
        # Define the backtracking function
        def backtrack(start, currentSubset):
            
            # Append a copy of the current subset to the result
            result.append(list(currentSubset))
            
            # Iterate over the possible elements to add to the subset
            for i in range(start, len(nums)):
                
                # Include nums[i] in the current subset
                currentSubset.append(nums[i])
                
                # Recurse with the updated subset
                backtrack(i + 1, currentSubset)
                
                # Backtrack by removing the last element added
                currentSubset.pop()
        
        # Start backtracking with an empty subset
        backtrack(0, [])
        
        # Return the list of all subsets
        return result