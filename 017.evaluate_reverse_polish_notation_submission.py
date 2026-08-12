class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numStack = []
        resultSoFar = None

        for token in tokens:
            if token not in "+-*/":
                numStack.append(int(token))
            
            else:
                # Going to assume that tokens is a valid representation
                # of a RPN expresion
                operand2 = numStack.pop()
                operand1 = numStack.pop()

                if token == "+":
                    numStack.append(operand1 + operand2)
                
                elif token == "-":
                    numStack.append(operand1 - operand2)
                
                elif token == "*":
                    numStack.append(operand1 * operand2)
                
                elif token == "/":
                    numStack.append(int(operand1 / operand2))
        
        return numStack.pop()