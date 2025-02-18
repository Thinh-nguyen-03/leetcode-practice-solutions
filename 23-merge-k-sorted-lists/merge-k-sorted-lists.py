# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, index, node))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, index, node = heapq.heappop(min_heap)
            
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        return dummy.next
