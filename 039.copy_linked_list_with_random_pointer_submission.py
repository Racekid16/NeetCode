# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # Step 1: Interleave copied nodes with original nodes
        # Original: A -> B -> C
        # After: A -> A' -> B -> B' -> C -> C'
        # so the corresponding copy node for each original node
        # is always right after the original node
        currentNode = head
        
        while currentNode is not None:
            newCopyNode = Node(currentNode.val)
            newCopyNode.next = currentNode.next
            currentNode.next = newCopyNode
            currentNode = newCopyNode.next

        # Step 2: Set the .random pointers of the copied nodes
        # Each copied node is currentNode.next
        currentOriginalNode = head
        while currentOriginalNode is not None:
            if currentOriginalNode.random is not None:
                correspondingCopyNode = currentOriginalNode.next
                correspondingRandomCopyNode = currentOriginalNode.random.next
                correspondingCopyNode.random = correspondingRandomCopyNode

            currentOriginalNode = currentOriginalNode.next.next

        # Step 3: Separate the original and copied nodes
        # Restore original list and extract copy list
        copyHead = head.next
        currentOriginalNode = head

        while currentOriginalNode is not None:
            correspondingCopyNode = currentOriginalNode.next
            currentOriginalNode.next = correspondingCopyNode.next  # restore original list
            currentOriginalNode = currentOriginalNode.next

            if currentOriginalNode is not None:
                correspondingCopyNode.next = currentOriginalNode.next  # set next for copied list

        return copyHead
