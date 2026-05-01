# leetcode problem 15: 3Sum
# Difficulty: Medium
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array first
        res = []
        
        for i, a in enumerate(nums):
            # Skip the same value in the previous position
            if i > 0 and a == nums[i - 1]:
                continue # continue to next loop iteration
            
            # Initilise left, right pointers (apply 2sumII)
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
    
# Test cases:
# Case 1: nums = [-1,0,1,2,-1,-4]
# Case 2: nums = []
# Case 3: nums = [0]

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [-1,0,1,2,-1,-4]
    nums2 = []
    nums3 = [0]
    
    print(sol.threeSum(nums1)) # should return [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum(nums2)) # should return []
    print(sol.threeSum(nums3)) # should return []