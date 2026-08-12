# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        previousResult = lists[0]

        for k in range(1, len(lists)):
            previousResult = self.mergeTwoLists(previousResult, lists[k])
        
        return previousResult
        
    # list1 and list2 must be sorted, not be cyclic, and not share any nodes.
    def mergeTwoLists(self, list1Head, list2Head):
        list1Ptr = list1Head
        list2Ptr = list2Head

        dummy = ListNode()
        previousNode = dummy

        while list1Ptr is not None and list2Ptr is not None:
            if list1Ptr.val <= list2Ptr.val:
                previousNode.next = list1Ptr
                previousNode = list1Ptr
                list1Ptr = list1Ptr.next
            else:
                previousNode.next = list2Ptr
                previousNode = list2Ptr
                list2Ptr = list2Ptr.next
        
        previousNode.next = list1Ptr if list1Ptr is not None else list2Ptr

        return dummy.next