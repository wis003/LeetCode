class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        i = 0
        while i <= (len(arr) / 2):
            if arr[i] != arr[len(arr) - i - 1]:
                return False 
            i += 1
        return True