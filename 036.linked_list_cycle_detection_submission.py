# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPtr = head
        fastPtr = head

        while fastPtr is not None and fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

            if slowPtr == fastPtr:
                return True
        
        return False