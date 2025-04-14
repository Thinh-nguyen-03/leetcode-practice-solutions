from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Count the frequency of each task
        taskCounts = Counter(tasks)
        
        # Create a max-heap based on task frequency
        maxHeap = [-count for count in taskCounts.values()]
        heapq.heapify(maxHeap)
        
        # Queue to manage cooldowns
        cooldownQueue = deque()
        
        # Total time intervals
        time = 0
        
        # While there are tasks to process
        while maxHeap or cooldownQueue:
            
            # Increment time for each interval
            time += 1
            
            if maxHeap:
                # Pop the most frequent task
                currentTaskCount = heapq.heappop(maxHeap) + 1
                
                # If there are more of this task, add to cooldown
                if currentTaskCount:
                    cooldownQueue.append((currentTaskCount, time + n))
            
            # Check if any task in cooldown is ready to be executed again
            if cooldownQueue and cooldownQueue[0][1] == time:
                heapq.heappush(maxHeap, cooldownQueue.popleft()[0])
        
        return time