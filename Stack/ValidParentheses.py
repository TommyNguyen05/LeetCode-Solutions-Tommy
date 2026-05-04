# Leetcode problem 20: Valid Parentheses
# Difficulty: Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "}": "{", "]": "[" }

        for char in s:
            # First check if the character is a closing parenthesis
            if char in closeToOpen:
                # If it is, check first if the stack is empty, and then check
                # if the the top of stack if its matching open bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False # immediately return false
            else: # if not then it's an opening bracket
                stack.append(char)
        return True if not stack else False
    
# Test cases:
# Case 1: s = "()" return True
# Case 2: s = "()[]{}" return True
# Case 3: s = "(]" return False
# Case 4: s = "([)]" return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()")) # True
    print(solution.isValid("()[]{}")) # True
    print(solution.isValid("(]")) # False
    print(solution.isValid("([)]")) # False
