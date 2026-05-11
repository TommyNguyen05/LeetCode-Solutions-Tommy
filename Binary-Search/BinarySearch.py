# Leetcode 704. Binary Search
# Difficulty: Easy
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
# Test cases:
# Case 1: nums = [-1,0,3,5,9,12], target = 9
# Case 2: nums = [-1,0,3,5,9,12], target = 2
# Case 3: nums = [-1,0,3,5,9,12], target = 3

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    
    nums3 = [-1,0,3,5,9,12]
    target3 = 3
    
    print(sol.search(nums1, target1)) # should return 4
    print(sol.search(nums2, target2)) # should return -1
    print(sol.search(nums3, target3)) # should return 2