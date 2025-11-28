# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
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