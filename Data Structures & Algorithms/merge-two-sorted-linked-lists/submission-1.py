# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the start of our new merged list
        dummy = ListNode()
        tail = dummy
        p1, p2 = list1, list2
        # While both lists still have nodes to compare
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        # If one list runs out, attach whatever is left of the other list
        if p1:
            tail.next = p1
        elif p2:
            tail.next = p2
        return dummy.next