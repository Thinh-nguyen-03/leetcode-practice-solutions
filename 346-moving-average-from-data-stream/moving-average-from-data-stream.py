from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.window_sum += val
        
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()
        
        return float(self.window_sum) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)