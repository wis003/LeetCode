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
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverseList(head)
        if n == 1:
            return self.reverseList(head.next)
        temp = head
        while n > 2:
            head = head.next
            n -= 1
        head.next = head.next.next
        return self.reverseList(temp)
            
