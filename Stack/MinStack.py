# leetcode problem 155: Min Stack
# Difficulty: Easy
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # To support getMin operation,
        
        # Note: to get top of stack (implemented using array) -> stack[-1]
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
# test cases:
# Case 1: ["MinStack","push","push","push","getMin","pop","top","getMin"]
#         [[],[-2],[0],[-3],[],[],[],[]]
# Case 2: ["MinStack","push","push","getMin","pop","top","getMin"]
#         [[],[1],[2],[],[],[],[]]

if __name__ == "__main__":
    minStack = MinStack()
    
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin()) # should return -3
    minStack.pop()
    print(minStack.top())    # should return 0
    print(minStack.getMin()) # should return -2
    
    minStack2 = MinStack()
    
    minStack2.push(1)
    minStack2.push(2)
    print(minStack2.getMin()) # should return 1
    minStack2.pop()
    print(minStack2.top())    # should return 1
    print(minStack2.getMin()) # should return 1