# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # algorithm: 
        # get the length of the list,
        # split the list into 2 halves,
        # reverse the second half,
        # interleave the halves
        # [0, 1, 2, 3, 4, 5, 6] ->
        # [0, 1, 2, 3], [4, 5, 6] ->
        # [0, 1, 2, 3], [6, 5, 4] ->
        # [0, 6, 1, 5, 2, 4, 3]
        forwardPtr = head

        # requires: head node
        # returns: length of the list
        # example: [0, 1, 2, 3, 4, 5, 6] -> 7
        def getListLen(head: ListNode) -> int:
            listLen = 0
            while head is not None:
                head = head.next
                listLen += 1
            return listLen
        
        # requires: head node, length of the list
        # effects: splits the list into two halves, disconnecting the halves
        # returns: the first node of the right half of the list
        # example: [0, 1, 2, 3, 4, 5, 6] -> [0, 1, 2, 3], [4, 5, 6]
        def splitList(head: ListNode, listLen: int) -> ListNode:
            if listLen % 2 == 0:    # even
                leftHalfLastNodeIndex = int(listLen / 2 - 1)
            else:
                leftHalfLastNodeIndex = listLen // 2

            currentNode = head

            for nodeIndex in range(leftHalfLastNodeIndex):
                currentNode = currentNode.next
            
            rightHalfFirstNode = currentNode.next
            currentNode.next = None

            return rightHalfFirstNode
        
        # requires: head node
        # effects: reverses the list 
        # returns: the new head node of the reversed list
        # example: [4, 5, 6] -> [6, 5, 4]
        def reverseList(head: ListNode) -> ListNode:
            previousNode = None
            currentNode = head

            while currentNode is not None:
                nextNode = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode
            
            return previousNode
        
        # requires: the head node of two different, unconnected lists
        # effects: interleaves the two lists into one merged list
        # returns: None
        # example: [0, 1, 2, 3], [6, 5, 4] -> [0, 6, 1, 5, 2, 4, 3]
        def interleaveLists(leftHalfHead: ListNode, rightHalfHead: ListNode) -> None:
            leftHalfCurrentNode = leftHalfHead
            rightHalfCurrentNode = rightHalfHead

            while rightHalfCurrentNode is not None:
                leftHalfNextNode = leftHalfCurrentNode.next
                rightHalfNextNode = rightHalfCurrentNode.next

                leftHalfCurrentNode.next = rightHalfCurrentNode
                rightHalfCurrentNode.next = leftHalfNextNode

                leftHalfCurrentNode = leftHalfNextNode
                rightHalfCurrentNode = rightHalfNextNode

        listLen = getListLen(head)
        if listLen == 1:
            return
        
        rightHalfFirstNode = splitList(head, listLen)
        rightHalfFirstNode = reverseList(rightHalfFirstNode)
        interleaveLists(head, rightHalfFirstNode)
