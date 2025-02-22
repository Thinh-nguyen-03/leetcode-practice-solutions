class Solution:
    def combinationSum(self, candidates, target):
        
        # Initialize the result list to store all valid combinations
        result = []
        
        # Define the backtrack function
        def backtrack(remainingTarget, combination, startIndex):
            
            # If the remaining target is zero, a valid combination is found
            if remainingTarget == 0:
                result.append(list(combination))
                return
            
            # Iterate over the candidates starting from the current index
            for i in range(startIndex, len(candidates)):
                
                # If the candidate exceeds the remaining target, skip further exploration
                if candidates[i] > remainingTarget:
                    continue
                
                # Add the candidate to the current combination
                combination.append(candidates[i])
                
                # Recursively call backtrack with the updated target and combination
                backtrack(remainingTarget - candidates[i], combination, i)
                
                # Remove the last candidate to backtrack
                combination.pop()
        
        # Start the backtracking process
        backtrack(target, [], 0)
        
        # Return the result containing all valid combinations
        return result