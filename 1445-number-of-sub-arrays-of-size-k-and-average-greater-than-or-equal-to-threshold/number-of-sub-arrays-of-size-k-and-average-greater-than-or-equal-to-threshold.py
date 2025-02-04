class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold_sum = k * threshold
        window_sum = sum(arr[:k])  # Initialize the sum of the first window
        count = 0

        # Check the first window
        if window_sum >= threshold_sum:
            count += 1

        # Slide the window across the array
        for i in range(k, len(arr)):
            # Update the window sum by sliding one element
            window_sum += arr[i] - arr[i - k]
            # Check if the current window satisfies the condition
            if window_sum >= threshold_sum:
                count += 1

        return count
