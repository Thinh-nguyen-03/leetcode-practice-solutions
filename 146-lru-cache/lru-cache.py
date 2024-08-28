from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.data = OrderedDict()  # OrderedDict to store the cache
        self.cap = capacity  # Maximum capacity of the cache

    def get(self, key: int) -> int:
        if key in self.data:
            # If the key is in the cache, move it to the end to mark it as recently used
            self.data.move_to_end(key)
            return self.data[key]
        else:
            # If the key is not in the cache, return -1
            return -1

    def put(self, key: int, value: int) -> None:
        # Insert the key-value pair, and move the key to the end to mark it as recently used
        self.data[key] = value
        self.data.move_to_end(key)
        
        # If the cache exceeds capacity, remove the least recently used item (first item)
        if len(self.data) > self.cap:
            self.data.popitem(last=False)
