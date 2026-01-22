import unittest
from group_anagrams import Solution

class TestGroupAnagrams(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def normalize(self, groups):
        return sorted(sorted(group) for group in groups)

    def test1(self):
        # output can be in any order
        result = self.normalize(self.s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        test_case = self.normalize([["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertEqual(result, test_case)

    def test2(self):
        self.assertEqual(self.s.groupAnagrams([""]), [[""]])

    def test3(self):
        self.assertEqual(self.s.groupAnagrams(["a"]), [["a"]])

if __name__ == "__main__":
    unittest.main()