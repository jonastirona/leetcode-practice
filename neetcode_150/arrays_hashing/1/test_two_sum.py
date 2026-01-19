import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_arr(self):
        self.assertIsNone(self.s.twoSum([], 0))

    def test_no_solution(self):
        self.assertIsNone(self.s.twoSum([1,2,3], 6))

    def test_valid_solution(self):
        self.assertEqual(self.s.twoSum([1,2,3], 5), [1,2])



if __name__ == "__main__":
    unittest.main()