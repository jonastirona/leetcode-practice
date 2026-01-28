import unittest
from product_except_self import Solution

class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.productExceptSelf([1,2,3,4]), [24,12,8,6])

    def test2(self):
        self.assertEqual(self.s.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

if __name__ == "__main__":
    unittest.main()