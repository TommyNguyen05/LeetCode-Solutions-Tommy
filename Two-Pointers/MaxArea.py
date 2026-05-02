# Leetcode problem 11: Container With Most Water
# Difficulty: Medium
# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area of the current container
            width = right - left
            current_area = min(heights[left], heights[right]) * width
            max_area = max(max_area, current_area)
            
            # Move the pointer that has the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
# Test cases:
# Case 1: heights = [1,8,6,2,5,4,8,3,7]
# Case 2: heights = [1,1]
# Case 3: heights = [4,3,2,1,4] 

if __name__ == "__main__":
    sol = Solution()
    
    heights1 = [1,8,6,2,5,4,8,3,7]
    heights2 = [1,1]
    heights3 = [4,3,2,1,4]
    
    print(sol.maxArea(heights1)) # should return 49
    print(sol.maxArea(heights2)) # should return 1
    print(sol.maxArea(heights3)) # should return 16