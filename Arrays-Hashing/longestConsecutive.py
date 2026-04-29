# leetcode 128. Longest Consecutive Sequence
# Difficulty: Medium
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# The algorithm should run in O(n) complexity.
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
# Test cases:
# Case 1: nums = [100,4,200,1,3,2]
# Case 2: nums = [3,7,2,5,8,4,6,0,1]

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [100,4,200,1,3,2]
    nums2 = [3,7,2,5,8,4,6,0,1]
    
    print(sol.longestConsecutive(nums1)) # should return 4
    print(sol.longestConsecutive(nums2)) # should return 8