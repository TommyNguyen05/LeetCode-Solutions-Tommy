# leetcode problem 238: Product of Array Except Self
# Difficulty: Medium
# Given an array nums of n integers, return an array output such that 
# output[i] is equal to the product of all the elements of nums except nums[i].
# Note: Please solve it without division and in O(n).

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initilise the output array
        result = [1] * len(nums)
        
        # compute with prefix from left to right
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        # compute post fix and multiply into the input array from right to left
        postfix = 1
        for i in range (len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
    
# Test cases:
# Case 1: nums = [1, 2, 3, 4]
# Case 2: nums = [-1, 1, 0, -3, 3]

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 1, 0, -3, 3]
    
    result1 = sol.productExceptSelf(nums1)
    result2 = sol.productExceptSelf(nums2)
    
    print(result1) # should return [24, 12, 8, 6]
    print(result2) # should return [0, 0, 9, 0, 0]