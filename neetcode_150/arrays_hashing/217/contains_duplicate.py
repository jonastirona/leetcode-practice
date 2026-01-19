# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Logic: use hashmap to keep track of seen nums, returning false if character has already been seen while iterating through num.
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums):
        map = defaultdict(int)

        for num in nums:
            if num in map: return True
            map[num] = 1

        return False
