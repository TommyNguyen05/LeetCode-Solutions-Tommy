# Leetcode problem 125: Valid Palindrome
# Difficulty: Easy
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and
# ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # building a new string that removes all non-alphanumeric character
        # newStr = ""
        
        # for c in s:
        #    if c.isalnum():
        #        newStr += c.lower()
        
        # return (newStr == newStr[::-1])
        # define two pointers left and right
        left, right = 0, len(s) - 1
        
        while left < right: # while the two pointers have not met
            # ensure both characters at left and right are alphanumeric
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            # only compare lowercase version of the character
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9'))

# Test cases:
# Case 1: s = " A man, a plan, a canal: Panama "
# Case 2: s = "race a car"

if __name__ == "__main__":
    sol = Solution()
    
    s1 = " A man, a plan, a canal: Panama "
    s2 = "race a car"
    print(sol.isPalindrome(s1)) # should return True
    print(sol.isPalindrome(s2)) # should return False
        
        