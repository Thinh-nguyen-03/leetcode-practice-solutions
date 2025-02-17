# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode()
        current_node = dummy_node
        carry = 0

        while l1 or l2 or carry:
            value_l1 = l1.val if l1 else 0
            value_l2 = l2.val if l2 else 0

            total = value_l1 + value_l2 + carry
            carry = total // 10

            current_node.next = ListNode(total % 10)
            current_node = current_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Ensure we are returning a valid ListNode
        if not isinstance(dummy_node.next, ListNode):
            raise TypeError("Return value is not a ListNode")

        return dummy_node.next
