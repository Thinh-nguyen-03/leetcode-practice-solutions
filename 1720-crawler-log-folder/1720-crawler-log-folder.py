class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
    
        count = 0
        
        for op in logs:
            if op == "../":
                if count > 0:
                    count -= 1
            elif op == "./":
                continue
            else:
                count += 1

        return count