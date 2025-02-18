# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited_node = set()
        current_node = head

        while current_node:
            if current_node in visited_node:
                return True

            visited_node.add(current_node)

            current_node = current_node.next

        return False
        