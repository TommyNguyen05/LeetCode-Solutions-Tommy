# leetcode problem 217: Contains Duplicate
# Difficulty: Easy
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

#Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using set data structure
        present = set()
        
        for num in nums:
            if num in present:
                return True
            # if not in the set
            present.add(num)
            
        return False
    
# testing the solution
# Case 1: nums = [1,2,3,3]
# Case 2: nums = [1,2,3,4]

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    
    print(sol.containsDuplicate(nums1)) # should return true
    print(sol.containsDuplicate(nums2)) # should return false
        
        