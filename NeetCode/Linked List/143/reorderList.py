# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> (ListNode, int):
        curr, pre = None, None
        count = 0
        while head:
            curr = head.next
            head.next = pre
            pre = head
            
            head = curr
            count += 1
        return pre, count
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        forward = deepcopy(head.next)
        reverse, total = self.reverseList(deepcopy(head))
        curr = head
        count = 0
        while count < total - 1:
            if count % 2 == 0:
                curr.next = reverse
                reverse = reverse.next
            else:
                curr.next = forward  
                forward = forward.next
            
            curr = curr.next
            count += 1
            if count == total - 1:
                curr.next = None
                     