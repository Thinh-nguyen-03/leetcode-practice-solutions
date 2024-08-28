class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key -> Node
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail  # Connect head to tail
        self.tail.prev = self.head  # Connect tail to head

    def _remove(self, node):
        # Remove a node from the linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        # Add a new node right after the head (front of the list)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value  # Update the value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove the least recently used node (from the tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            # Add the new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
