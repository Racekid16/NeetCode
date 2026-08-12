class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add all words to trie
        root = TrieNode()

        for word in words:
            currentNode = root
            for charPos in range(len(word)):
                char = word[charPos]
                if char not in currentNode.children:
                    currentNode.children[char] = TrieNode()
                currentNode = currentNode.children[char]
            currentNode.endOfWords.append(word)

        foundWords = set()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        # search grid for words
        def dfs(row, col, currentNode):
            if row < 0 or row > len(board) - 1 \
            or col < 0 or col > len(board[0]) - 1 \
            or visited[row][col]:
                return

            visited[row][col] = True
            char = board[row][col]

            if char not in currentNode.children:
                visited[row][col] = False
                return
            
            for word in currentNode.children[char].endOfWords:
                foundWords.add(word)
            
            dfs(row - 1, col, currentNode.children[char])
            dfs(row + 1, col, currentNode.children[char])
            dfs(row, col - 1, currentNode.children[char])
            dfs(row, col + 1, currentNode.children[char])
            
            visited[row][col] = False

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root)
        
        return list(foundWords)

        
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWords = []