# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        leftPtr = head
        rightPtr = head

        for _ in range(n):
            rightPtr = rightPtr.next
  
        if rightPtr is None:
            return head.next
        
        while rightPtr.next is not None:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next

        leftPtr.next = leftPtr.next.next
        return head