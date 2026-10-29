''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count