# leetcode problem 853: car fleet
# Difficulty: Medium
# N cars are going to the same destination along a one lane road.  The destination is target miles away.
# Each car i has a constant speed speed[i] (in miles per hour) and initial position position[i] miles towards the target along the road.
# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at
# the same speed.  The distance between these two cars is ignored - they are assumed to have the same position.
# A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.
# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
# How many car fleets will arrive at the destination?

from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # creating list of pairs [postion, speed]
        pair = [[p, s] for p, s in zip(position, speed)]
        # stack use to track how many car fleet reach the taget
        stack = []
        
        # loop through the pair in Reversed SORTED order
        for p, s in sorted(pair)[::-1]:
            # calculate what time the car reach the destination and add to stack to track for overlap
            stack.append((target - p) / s)
            # check if the stack has at least two elements (bc one element wouldn't result in anything)
            # and if the car before the one ahead would reach the target first, means they collide and become
            # ONE car fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Test cases:
# Case 1: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Case 2: target = 10, position = [3], speed = [3]
# Case 3: target = 100, position = [0,2,4], speed = [4,2,1]

if __name__ == "__main__":
    sol = Solution()
    
    target1 = 12
    position1 = [10,8,0,5,3]
    speed1 = [2,4,1,1,3]
    
    target2 = 10
    position2 = [3]
    speed2 = [3]
    
    target3 = 100
    position3 = [0,2,4]
    speed3 = [4,2,1]
    
    print(sol.carFleet(target1, position1, speed1)) # should return 3
    print(sol.carFleet(target2, position2, speed2)) # should return 1
    print(sol.carFleet(target3, position3, speed3)) # should return 1