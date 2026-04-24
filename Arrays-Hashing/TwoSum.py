# leetcode problem 1: Two Sum
# Difficulty: Easy
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force approach: check every pair of numbers to see if they add up to target
        # Time complexity: O(n^2)
        # nums[i] + nums[j] = target
        
        # For this number, what do I need to add to it to get the target? 
        # target - nums[i]
        # Hash map approach: store the numbers in a hash map and check if the complement (target - current number) exists in the hash map
        # Time complexity: O(n) (for O(n) of looking up element in map)
        
        seen = {}
        
        for i, num in enumerate(nums):
            neededNum = target - num
            
            if neededNum in seen:
                return [seen[neededNum], i]
            seen[num] = i
            
# testing cases
# Case 1: nums = [2,7,11,15], target = 9
# Case 2: nums = [3,2,4], target = 6
# Case 3: nums = [3,3], target = 6

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [2, 7, 11, 15]
    target1 = 9
    
    nums2 = [3, 2, 4]
    target2 = 6
    
    nums3 = [3, 3]
    target3 = 6
    
    print(sol.twoSum(nums1, target1)) # should return [0, 1]
    print(sol.twoSum(nums2, target2)) # should return [1, 2]
    print(sol.twoSum(nums3, target3)) # should return [0, 1]