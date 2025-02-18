# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def enough_nodes(start, k):
            count = 0
            while start and count < k:
                start = start.next
                count += 1
            return count == k

        def reverse(start, k):
            prev = None
            current = start
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while enough_nodes(group_prev.next, k):
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next

            group_end.next = None
            group_prev.next = reverse(group_start, k)

            group_start.next = next_group_start

            group_prev = group_start

        return dummy.next
        