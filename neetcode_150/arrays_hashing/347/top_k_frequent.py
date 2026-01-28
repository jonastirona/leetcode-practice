# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order
# logic: count freqs of all nums, push all (freq, num) to heap so it sorts by freq, then return first k elements of heap)

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        freqs = defaultdict(int)

        for num in nums:
            freqs[num]+=1

        top = []

        for num in freqs:
            heapq.heappush(top, (-freqs[num], num))

        result = []

        for i in range(k):
            current = heapq.heappop(top)
            result.append(current[1])

        return result