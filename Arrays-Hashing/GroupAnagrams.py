# leetcode problem 49: Group Anagrams
# Difficulty: Medium
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}
        
        for word in strs:
            # initialise counting array
            count = [0] * 26
            # check each character in a word
            for c in word:
                # index the corresponding character and update the count
                count[ord(c) - ord('a')] += 1
                
            # convery the count array into tuple (key in dictionary can't be changed in any ways) to use as key
            key = tuple(count)
            
            if key not in anagramGroups:
                anagramGroups[key] = []
            
            anagramGroups[key].append(word)
            
        return list(anagramGroups.values())
    
    # Test cases:
    # Case 1: strs = ["eat","tea","tan","ate","nat","
    # Case 2: strs = [""]
    # Case 3: strs = ["a"]
    
if __name__ == "__main__":
    sol = Solution()
    
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = [""]
    strs3 = ["a"]
    
    print(sol.groupAnagrams(strs1)) # should return [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(sol.groupAnagrams(strs2)) # should return [[""]]
    print(sol.groupAnagrams(strs3)) # should return [["a"]]