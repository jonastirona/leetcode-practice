# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Logic: First, if they are differing lengths return false. If they are both empty, return True. Second, use hashmap to store (character, count) for word 1. then, iterate through word 2 and for each character, if exists in hashmap, decrement the count. if the count < 0 (the letter occurs more in word 2) or the character doesn't exist in hashmap, return false. also return false if at the end of iterating through word 2, the count of a character in hasmap > 0. If not all that, return True. 
from collections import defaultdict

class Solution:
    def isAnagram(self, s, t):
        if len(s) == 0 and len(t) == 0: return True
        if len(s) != len(t): return False

        s_count = defaultdict(int)

        for char in s:
            s_count[char]+=1

        for char in t:
            if char not in s_count: return False
            s_count[char]-=1
            if s_count[char] < 0: return False
        
        return True