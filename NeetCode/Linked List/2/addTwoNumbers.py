# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        decimal = 0
        while l1 or l2:
            if l1 and not l2:
                total += l1.val * (10 ** decimal)
                l1 = l1.next
            elif l2 and not l1:
                total += l2.val * (10 ** decimal)
                l2 = l2.next
            else:
                total += l1.val * (10 ** decimal)
                l1 = l1.next
                total += l2.val * (10 ** decimal)
                l2 = l2.next
            decimal += 1
        
        if total == 0:
            return ListNode(val = 0)
        temp = ListNode
        pre = temp
        while total > 0:
            curr = ListNode(val = total % 10)
            pre.next = curr
            pre = curr
            total = total // 10
        return temp.next
