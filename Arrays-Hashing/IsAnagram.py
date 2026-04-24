# leetcode problem 242: Valid Anagram
# Difficulty: Easy
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case: if the lengths of the strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Creating a dictionary/or hash map of count that first count the letters in s,
        # and then subtract the count of each letter when scanning t string, if they all zeros, they're anagrams
        
        # initalise dictionary
        count = {}
        
        for char in s:
            # if that character is not in count
            if char not in count:
                count[char] = 0 # add that character with inital count of 0
            count[char] += 1
        
        for char in t:
            # if the character of the next string is not in count, they're not anagrams
            if char not in count:
                return False
            count[char] -= 1
            
            # if a character appears more time, it would minus to negative
            if count[char] < 0:
                return False
        # No distruption, so they're anagrams
        return True
    
    # Test cases:
    # Case 1:
    # s = "racecar"
    # t = ""carrace"
    
    # Case 2:
    # s = "jar"
    # t = "jam"
    
if __name__ == "__main__":
    sol = Solution()
    s1 = "racecar"
    t1 = "carrace"
    
    s2 = "jar"
    t2 = "jam"
    
    print(sol.isAnagram(s1, t1))
    print(sol.isAnagram(s2, t2))
        