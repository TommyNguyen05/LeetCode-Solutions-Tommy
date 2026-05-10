# leetcode 

from ast import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack to keep track of the index of the bars
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            # while the current bar is smaller than the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                # pop the top of the stack and calculate the area
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        # calculate area for remaining bars in stack
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area