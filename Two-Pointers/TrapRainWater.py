# Leetcode problem 42: Trapping Rain Water
# Difficulty: Hard
# Given n non-negative integers representing an elevation map where the width of each bar is 1
# compute how much water it can trap after raining.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped_water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += max(0, right_max - height[right])
        
        return trapped_water
    
# Test cases:
# Case 1: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Case 2: height = [4,2,0,3,2,5]
# Case 3: height = [0,0,0,0,0]

if __name__ == "__main__":
    sol = Solution()
    
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    height2 = [4,2,0,3,2,5]
    height3 = [0,0,0,0,0]
    
    print(sol.trap(height1)) # should return 6
    print(sol.trap(height2)) # should return 9
    print(sol.trap(height3)) # should return 0