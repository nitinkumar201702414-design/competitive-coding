class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next