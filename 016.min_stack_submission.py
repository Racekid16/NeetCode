class MinStack:

    def __init__(self):
        self.minValBelowStack = []
        self.stack = []

    def push(self, val: int) -> None:
        oldStackLen = len(self.stack)
        self.stack.append(val)

        if oldStackLen == 0:
            self.minValBelowStack.append(val)
        else:
            self.minValBelowStack.append(min(val, self.minValBelowStack[oldStackLen - 1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minValBelowStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minValBelowStack[len(self.minValBelowStack) - 1]
