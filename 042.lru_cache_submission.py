class LRUCache:
    # idea: store values in a linked list
    # where the most recently used is right before the dummy tail
    # and the least recently used is right after the dummy head.
    # also keep a dictionary mapping keys to nodes.
    class DoublyLinkedListNode:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}

        # create dummy head and tail
        self.head = self.DoublyLinkedListNode(0, 0)
        self.tail = self.DoublyLinkedListNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]
        self.removeNode(node)
        self.insertNodeAtFront(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.value = value
            self.removeNode(node)
            self.insertNodeAtFront(node)
        else:
            if len(self.keyToNode) == self.capacity:
                self.removeLeastRecentlyUsedNode()

            newNode = self.DoublyLinkedListNode(key, value)
            self.keyToNode[key] = newNode
            self.insertNodeAtFront(newNode)

    def insertNodeAtFront(self, node):
        # insert right before tail
        prevNode = self.tail.prev
        nextNode = self.tail

        prevNode.next = node
        node.prev = prevNode

        node.next = nextNode
        nextNode.prev = node

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def removeLeastRecentlyUsedNode(self):
        # least recently used node is the one right after dummy head
        lruNode = self.head.next
        self.removeNode(lruNode)
        del self.keyToNode[lruNode.key]
