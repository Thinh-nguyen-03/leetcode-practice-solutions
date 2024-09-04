from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlog(n)) solution
        # # Step 1: Count the frequency of each element
        freq_map = Counter(nums)
        
        # Step 2: Use a heap to extract the top k frequent elements
        # We use a heap with (-frequency, num) so that we can extract the most frequent elements
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (-freq, num))
        
        # Step 3: Extract the top k elements from the heap
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        # O(n) solution
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res
