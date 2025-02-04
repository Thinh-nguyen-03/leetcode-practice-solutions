class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}  # Dictionary to store the index of each number

        for i, num in enumerate(nums):
            if num in num_indices and i - num_indices[num] <= k:
                return True
            # Update the latest index of the number
            num_indices[num] = i

        return False
