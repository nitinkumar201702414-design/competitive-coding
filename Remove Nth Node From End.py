class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast n+1 steps ahead so the gap between fast and slow is n nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast falls off the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now just before the node to remove
        slow.next = slow.next.next
        return dummy.next