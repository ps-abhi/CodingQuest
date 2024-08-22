# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        combined = ''
        while current:
            combined=combined+str(current.val)
            current=current.next
        return int(combined, 2)

    