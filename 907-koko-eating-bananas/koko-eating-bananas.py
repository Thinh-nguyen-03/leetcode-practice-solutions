import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed = mid
            total_hours = sum(math.ceil(pile / mid) for pile in piles)

            if total_hours <= h:
                right = mid  # Try smaller k
            else:
                left = mid + 1  # Increase k
        
        return left
