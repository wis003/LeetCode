# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 and not list2:
            head = list1
            list1 = list1.next
        elif not list1 and list2:
            head = list2
            list2 = list2.next
        elif list1 and list2:
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        
        ret = head
        
        while head:
            if list1 and not list2:
                head.next = list1
                list1 = list1.next
            elif not list1 and list2:
                head.next = list2
                list2 = list2.next
            elif list1 and list2:
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
            head = head.next
        return ret
            
        