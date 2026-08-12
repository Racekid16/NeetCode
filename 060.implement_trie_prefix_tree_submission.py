class PrefixTree:

    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False 

    def insert(self, word: str) -> None:
        currentNode = self

        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = PrefixTree()
            currentNode = currentNode.children[char]
        
        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self

        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        
        return currentNode.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        currentNode = self

        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        
        return True
        
