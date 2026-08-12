# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        list1Ptr = list1
        list2Ptr = list2

        mergedListHead = None
        mergedListPtr = None
        
        if list1Ptr.val <= list2Ptr.val:
            mergedListHead = list1Ptr
            list1Ptr = list1Ptr.next
        else:
            mergedListHead = list2Ptr
            list2Ptr = list2Ptr.next
        
        mergedListPtr = mergedListHead

        while list1Ptr is not None and list2Ptr is not None:
            if list1Ptr.val <= list2Ptr.val:
                mergedListPtr.next = list1Ptr
                list1Ptr = list1Ptr.next

            else:  # list2Ptr.val < list1Ptr.val
                mergedListPtr.next = list2Ptr
                list2Ptr = list2Ptr.next

            mergedListPtr = mergedListPtr.next
    
        mergedListPtr.next = list1Ptr if list1Ptr is not None else list2Ptr
        
        return mergedListHead