# leetcode problem 347: Top K Frequent Elements
# difficulty: medium
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash map/dictionary to store the frequency of each element in the array
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
                
        # create a list that its indices represent the frequency and 
        # its values represent the elements with that frequency
        # the list is of size n + 1 because the maximum frequency of any element can be n
        buckets = [[] for _ in range(len(nums) + 1)] # a list of n + 1 empty lists
        
        for num, freq in frequency.items():
            buckets[freq].append(num) # add the element to the list at index freq
            
        # create a result list to store the k most frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

# Test cases:
# Case 1: nums = [1,1,1,2,2,3], k = 2
# Case 2: nums = [1], k = 1

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    nums2 = [1]
    k2 = 1
    
    print(sol.topKFrequent(nums1, k1)) # should return [1, 2]
    print(sol.topKFrequent(nums2, k2)) # should return [1]
