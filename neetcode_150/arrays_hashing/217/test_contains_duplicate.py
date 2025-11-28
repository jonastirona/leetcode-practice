import unittest
from contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_no_duplicate(self):
        self.assertFalse(self.s.containsDuplicate([1,2,3,4,5]))

    def test_duplicate(self):
        self.assertTrue(self.s.containsDuplicate([1,2,3,4,4]))
    
    def test_empty(self):
        self.assertFalse(self.s.containsDuplicate([]))

    def test_long_input(self):
        nums = list(range(0, 10000))
        nums.append(4)
        self.assertTrue(self.s.containsDuplicate(nums))

if __name__ == "__main__":
    unittest.main()