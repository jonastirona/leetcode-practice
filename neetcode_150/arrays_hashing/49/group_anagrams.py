# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Logic: use hashmap. key: sorted letter combo. value: list of anagrams that when sorted, match the key.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))

            anagrams[sortedWord].append(word)

        return list(anagrams.values())