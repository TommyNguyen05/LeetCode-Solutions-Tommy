# Leetcode problem 271: Encode and Decode Strings
# Difficulty: Medium
# Design an algorithm to encode a list of strings to a string. The encoded string is then 
# sent over the network and is decoded back to the original list of strings.

from typing import List

# string encoded in the form <<size of string>><<"#">>string
# example: ["Hello", "World"]
# encoded string: 5#Hello5#World

class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialise the resulted string
        result = ""
        
        # go string by string in the strs list
        for word in strs:
            # note: convert all type into string
            result += str(len(word)) + "#" + word # concatinate strings
        return result

    def decode(self, s: str) -> List[str]:
        # initialise the result array of strings
        result = []
        i = 0 # pointer to track the position so far in the string
        
        # while i is still inbound of the string s
        while i < len(s):
            # initiliase the second pointer j to track the delimiter(starting at the same position as i)
            j = i
            while s[j] != "#":
                j += 1
            # found the length of the string
            length = int(s[i:j]) # from i to j (BUT NOT INCLUDING J)
            result.append(s[j + 1 : j + 1 + length]) # append the actual string
            
            # updating i
            i = j + 1 + length
        return result
    
# Test cases:
# Case 1: strs = ["Hello", "World"]
# Case 2: strs = ["", "a", "bc"]

if __name__ == "__main__":
    sol = Solution()
    
    strs1 = ["Hello", "World"]
    strs2 = ["", "a", "bc"]
    
    encoded1 = sol.encode(strs1)
    decoded1 = sol.decode(encoded1)
    
    encoded2 = sol.encode(strs2)
    decoded2 = sol.decode(encoded2)
    
    print(encoded1) # should return "5#Hello5#World"
    print(decoded1) # should return ["Hello", "World"]
    
    print(encoded2) # should return "0##1#a2#bc"
    print(decoded2) # should return ["", "a", "bc"] 