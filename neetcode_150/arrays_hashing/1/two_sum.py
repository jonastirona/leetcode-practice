# Given an array of integers and an integer target, return the indices of the two numbers such that they add up to the target.
# Logic - iterate through array, storing each num in a hashmap where key = num and value = index. If the complement (target - current number) is already in the hashmap, then we found the two numbers that add up to target.

class Solution:
    def twoSum(self, nums, target):
        complements = {}

        for i, num in enumerate(nums):
            if target - num in complements:
                return [complements[target - num], i]
            complements[num] = i

        return None