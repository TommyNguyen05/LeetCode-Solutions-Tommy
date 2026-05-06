# Leetcode 150. Evaluate Reverse Polish Notation
# Difficulty: Medium
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression
# in Reverse Polish Notation.

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialise a stack
        stack = []
        for element in tokens:
            if element == "+":
                stack.append(stack.pop() + stack.pop())
            elif element == "-":
                # for correct subtraction
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif element == "*":
                stack.append(stack.pop() * stack.pop())
            elif element == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(element))
        return stack[0]

# Test cases:
# Case 1: tokens = ["2","1","+","3","*"]
# Case 2: tokens = ["4","13","5","/","+"]
# Case 3: tokens = ["10","6","9","3","+","-11","*","/","*"]

if __name__ == "__main__":
    sol = Solution()
    
    tokens1 = ["2","1","+","3","*"]
    tokens2 = ["4","13","5","/","+"]
    tokens3 = ["10","6","9","3","+","-11","*","/","*"]
    
    print(sol.evalRPN(tokens1)) # should return 9
    print(sol.evalRPN(tokens2)) # should return 4
    print(sol.evalRPN(tokens3)) # should return 22