import math
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Q1: Spiral Matrix - O(m*n)
def spiral_order(matrix: List[List[int]]) -> List[int]:
    res = []
    if not matrix:
        return res
    top, bot = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bot and left <= right:
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bot + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bot:
            for j in range(right, left - 1, -1):
                res.append(matrix[bot][j])
            bot -= 1
        if left <= right:
            for i in range(bot, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


# Q2: Sort an Array - Merge Sort, O(n log n)
def sort_array(a: List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = sort_array(a[:mid]), sort_array(a[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Q3: Remove Duplicates from a Sorted List - O(n)
def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


# Q4: Add Two Numbers as Linked Lists (digits in reverse order)
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next


# Q5: Minimum Banana-Eating Speed - Binary search, O(n log max)
def min_eating_speed(piles: List[int], h: int) -> int:
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


# Q6: Design a Singly Linked List
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def add_at_head(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size += 1

    def add_at_tail(self, val: int) -> None:
        self.add_at_index(self.size, val)

    def add_at_index(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.add_at_head(val)
            return
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        prev.next = ListNode(val, prev.next)
        self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
        self.size -= 1


# ---------- helpers + tests ----------
def build(values):
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))   # [1,2,3,6,9,8,7,4,5]
    print(sort_array([5, 2, 3, 1, 9, 4]))                    # [1,2,3,4,5,9]
    print(to_list(delete_duplicates(build([1, 1, 2, 3, 3]))))  # [1,2,3]
    print(to_list(add_two_numbers(build([2, 4, 3]), build([5, 6, 4]))))  # [7,0,8]
    print(min_eating_speed([3, 6, 7, 11], 8))                # 4

    ll = MyLinkedList()
    ll.add_at_head(1)
    ll.add_at_tail(3)
    ll.add_at_index(1, 2)
    print(ll.get(1))        # 2
    ll.delete_at_index(1)
    print(ll.get(1))        # 3