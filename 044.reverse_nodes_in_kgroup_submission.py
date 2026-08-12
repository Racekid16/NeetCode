# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        previousGroupTail = dummy
        currentGroupHead = head

        # at this point, previousGroupTail and currentGroupHead
        # need to be correctly set
        while currentGroupHead is not None:
            currentNode = currentGroupHead

            # find the tail of the current group
            count = 1
            while count < k and currentNode is not None:
                currentNode = currentNode.next
                count += 1

            # if fewer than k nodes remain, stop
            if currentNode is None:
                previousGroupTail.next = currentGroupHead
                break

            # cut the group
            nextGroupHead = currentNode.next
            currentNode.next = None

            # reverse current group
            currentGroupNewHead = self.reverseList(currentGroupHead)
            currentGroupNewTail = currentGroupHead

            # connect previous group to current group
            previousGroupTail.next = currentGroupNewHead

            # correctly set previousGroupTail and currentGroupHead
            previousGroupTail = currentGroupNewTail
            currentGroupHead = nextGroupHead

        return dummy.next

    def reverseList(self, head):
        previousNode = None
        currentNode = head

        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode

            previousNode = currentNode
            currentNode = nextNode

        return previousNode
