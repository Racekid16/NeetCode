# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummyHead is not really the head of the result,
        # but a dummy that is there just to create a starting point
        # for the result. The eventual result list will start at dummyHead.next
        dummyHead = ListNode(0)
        previousNode = dummyHead
        
        carry = 0
        l1CurrentNode = l1
        l2CurrentNode = l2
        
        # add corresponding digits from both lists
        while l1CurrentNode is not None or l2CurrentNode is not None or carry != 0:
            val1 = l1CurrentNode.val if l1CurrentNode is not None else 0
            val2 = l2CurrentNode.val if l2CurrentNode is not None else 0
            
            digitSum = val1 + val2 + carry
            carry = digitSum // 10
            newDigit = digitSum % 10
            
            # append new digit to result list
            previousNode.next = ListNode(newDigit)
            previousNode = previousNode.next
            
            # advance input pointers if possible
            if l1CurrentNode is not None:
                l1CurrentNode = l1CurrentNode.next
            if l2CurrentNode is not None:
                l2CurrentNode = l2CurrentNode.next
        
        return dummyHead.next
