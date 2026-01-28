from pickletools import read_unicodestringnl
import unittest
from top_k_frequent import Solution

class TestTopKFrequent(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        self.assertEqual(sorted((self.s.topKFrequent([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5], 3))), [3,4,5])

    def test2(self):
        self.assertEqual(self.s.topKFrequent([1],1), [1])

    def test3(self):
        self.assertEqual(self.s.topKFrequent([1,2,3],2), [1,2])

    def test4(self):
        self.assertEqual(self.s.topKFrequent([1,2,3,4,4,4],1),[4])

if __name__ == "__main__":
    unittest.main()