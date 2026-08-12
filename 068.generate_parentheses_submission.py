class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # General backtrack pattern:
        # - define a recursive function
        #   - inputs to the function are the current state
        #   - return if current state is a valid solution
        #   - recursive calls pass in next state
        # - call the recursive function with the start state

        # Given a current string (this defines the current path):
        # - it is a solution if numOpen == n and numClose == n
        # - it can add an open parenthesis if numOpen < n
        # - it can add a close parenthesis if numClose < numOpen
        # The current string can be represented as a stack since we always add/remove
        # to the end of the current string

        # On a specific path, 3 things are variable:
        # - the current string
        # - the number of open parenthesis
        # - the number of close parentheis
        # a path ends when the base case is hit.
        # otherwise, there either is only one possible continuation path,
        # or it can fork into two possible continuation paths
        res = []

        def backtrack(curr, numOpen, numClose):
            # base case
            if numOpen == n and numClose == n:
                res.append("".join(curr))
            
            # recursive cases- gets you one step closer to base case
            else:
                if numOpen < n:
                    curr.append("(")
                    backtrack(curr, numOpen + 1, numClose)
                    curr.pop()
                
                if numClose < numOpen:
                    curr.append(")")
                    backtrack(curr, numOpen, numClose + 1)
                    curr.pop()
    
        backtrack([], 0, 0)

        return res