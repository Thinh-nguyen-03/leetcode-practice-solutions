# # Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Step 1: Create a mapping from original nodes to new nodes
        node_map = {}
        current = head

        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # Step 2: Assign next and random pointers
        current = head
        while current:
            new_node = node_map[current]
            new_node.next = node_map.get(current.next, None)
            new_node.random = node_map.get(current.random, None)
            current = current.next

        return node_map[head]
