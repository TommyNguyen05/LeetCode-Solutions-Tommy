# leetcode 167. Two Sum II - Input Array Is Sorted
# Difficulty: Easy
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
                
# Test cases:
# Case 1: numbers = [2,7,11,15], target = 9
# Case 2: numbers = [2,3,4], target = 6
# Case 3: numbers = [-1,0], target = -1

if __name__ == "__main__":
    sol = Solution()
    
    numbers1, target1 = [2,7,11,15], 9
    numbers2, target2 = [2,3,4], 6
    numbers3, target3 = [-1,0], -1
    
    print(sol.twoSum(numbers1, target1)) # should return [1, 2]
    print(sol.twoSum(numbers2, target2)) # should return [1, 3]
    print(sol.twoSum(numbers3, target3)) # should return [1, 2]