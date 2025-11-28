import unittest
from valid_anagram import Solution

class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_anagram(self):
        self.assertTrue(self.s.isAnagram("abc", "cba"))

    def test_not_anagram(self):
        self.assertFalse(self.s.isAnagram("abc", "abd"))

    def test_long_input(self):
        self.assertTrue(self.s.isAnagram("aoirsetnmoumwnfougnmouanrsmtounmoucnokvuhousmoausnroutomwaoersmtomuarsngkouawfkoguakoukdouvklrokguiacmfouglokuavrpmlgocauirkflgovuyacrmlfoguyklaomcywufxpklgaulkrshtuklvhuwlkfhulhulk", "iacmfouglokuavrpmlgocauirkflgovuyacrmlfoguyklaomcywufxpklgaulkrshtuklvhuwlkfhulhulkaoirsetnmoumwnfougnmouanrsmtounmoucnokvuhousmoausnroutomwaoersmtomuarsngkouawfkoguakoukdouvklrokgu"))

    def test_incorrect_long_input(self):
        self.assertFalse(self.s.isAnagram("aoirsetnmoumwnfougnmouanrsmtounmoucnokvuhousmoausnroutomwaoersmtomuarsngkouawfkoguakoukdouvklrokguiacmfouglokuavrpmlgocauirkflgovuyacrmlfoguyklaomcywufxpklgaulkrshtuklvhuwlkfhulhulk", "iacmfouglokuavrpmlgocauirkflgovuyacrmlfoguyklaomcywufxpklgaulkrshtuklvhuwlkfhulhulkaoirsetnmoumwnfougnmouanrsmtounmoucnokvuhousmoausnroutomwaoersmtomuarangkouawfkoguakoukdouvklrokgu"))

    def test_different_len(self):
        self.assertFalse(self.s.isAnagram("ab", "abc"))
    
    def test_one_char(self):
        self.assertTrue(self.s.isAnagram("a", "a"))

    def test_one_char_false(self):
        self.assertFalse(self.s.isAnagram("a", "b"))
    
    def test_empty(self):
        self.assertTrue(self.s.isAnagram("", ""))

if __name__=="__main__":
    unittest.main()