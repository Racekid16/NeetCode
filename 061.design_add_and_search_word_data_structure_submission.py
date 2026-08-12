class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root

        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        
        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:

        def dfs(currentNode, word):

            for charPos in range(len(word)):
                char = word[charPos]

                if char == ".":
                    for charKey in currentNode.children:
                        if dfs(currentNode.children[charKey], word[charPos+1:]):
                            return True
                    
                    return False

                if char not in currentNode.children:
                    return False
                
                currentNode = currentNode.children[char]
            
            return currentNode.isEndOfWord
        
        return dfs(self.root, word)
                

class TrieNode:
    def __init__(self):
        # dictionary of TrieNodes representing the next letter
        self.children = dict()
        self.isEndOfWord = False
