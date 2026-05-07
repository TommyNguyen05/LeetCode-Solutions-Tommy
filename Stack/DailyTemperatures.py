# leetcode problem 739: daily temperatures
# Difficulty: Medium
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there
# is no future day for which this is possible, put 0 instead.

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        # This solution uses monotonic decreasing stack to rememeber the days (difference in indices)
        # that are still waiting for warming temperature
        stack = [] # a pair of [temp, index] to calculate the difference in the indices
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append([t, i])
        return res
    
# Test cases:
# Case 1: temperatures = [73,74,75,71,69,72]
# Case 2: temperatures = [30,40,50,60]
# Case 3: temperatures = [30,60,90]

if __name__ == "__main__":
    sol = Solution()
    
    temperatures1 = [73,74,75,71,69,72]
    temperatures2 = [30,40,50,60]
    temperatures3 = [30,60,90]
    
    print(sol.dailyTemperatures(temperatures1)) # should return [1,1,4,2,1,0]
    print(sol.dailyTemperatures(temperatures2)) # should return [1,1,1,0]
    print(sol.dailyTemperatures(temperatures3)) # should return [1,1,0]