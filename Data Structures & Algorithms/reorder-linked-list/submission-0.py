class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 'slow' is now at the middle. Split the list into two halves.
        # second half starts at slow.next
        curr = slow.next
        slow.next = None  # Cut off the first half from the second half
        # Step 2: Reverse the second half
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Now 'prev' is the head of the reversed second half
        # Step 3: Merge the two halves alternately
        first, second = head, prev
        while second:
            # Temporarily save the next pointers
            tmp1, tmp2 = first.next, second.next
            # Interleave the nodes
            first.next = second
            second.next = tmp1
            # Advance pointers
            first = tmp1
            second = tmp2