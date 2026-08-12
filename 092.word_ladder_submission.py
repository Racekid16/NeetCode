class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # think of the words as nodes
        # words that are one character different are connected by an edge
        # find the shortest path between beginWord and endWord (use BFS)
        # Q: how can we quickly determine that two nodes should be neighbors?
        
        wordSet = set(wordList)
        
        def bfs(beginWord):
            visited = set()
            visited.add(beginWord)

            q = deque()
            q.append((beginWord, 1))

            while len(q) > 0:
                word, dist = q.popleft()

                if word == endWord:
                    return dist

                for pos in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:pos] + char + word[pos + 1:]
                        if (
                            newWord != word and
                            newWord in wordSet and
                            newWord not in visited
                        ):
                            visited.add(newWord)
                            q.append((newWord, dist + 1))
                            
            return 0

        return bfs(beginWord)