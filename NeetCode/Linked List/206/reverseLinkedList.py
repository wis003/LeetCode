# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, pre = None, None
        while head:
            curr = head.next
            head.next = pre
            pre = head
            
            head = curr
        return pre
        