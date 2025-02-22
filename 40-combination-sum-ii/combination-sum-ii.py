class Solution:
    def combinationSum2(self, candidates, target):
        
        def backtrack(startIndex, currentCombination, currentSum):
            
            if currentSum == target:
                result.append(list(currentCombination))
                return
            
            if currentSum > target:
                return
            
            for i in range(startIndex, len(candidates)):
                
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                
                currentCombination.append(candidates[i])
                
                backtrack(i + 1, currentCombination, currentSum + candidates[i])
                
                currentCombination.pop()
        
        candidates.sort()
        
        result = []
        
        backtrack(0, [], 0)
        
        return result