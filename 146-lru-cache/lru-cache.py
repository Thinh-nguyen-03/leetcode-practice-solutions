from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()  # Initialize an empty OrderedDict
        self.capacity = capacity    # Store the capacity of the cache

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Manually move the accessed key to the end to mark it as most recently used
            value = self.cache.pop(key)
            self.cache[key] = value  # Reinsert the key to move it to the end
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Remove the existing entry
            self.cache.pop(key)
        self.cache[key] = value  # Insert the key-value pair

        # If the cache exceeds its capacity, pop the first item (least recently used)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
