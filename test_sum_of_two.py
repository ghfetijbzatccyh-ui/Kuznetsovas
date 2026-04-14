import unittest
from sum_of_two import two_sum

class TestTwoSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(two_sum([2,7,11,15], 9), [0,1])

    def test_2(self):
        self.assertEqual(two_sum([3,2,4], 6), [1,2])

    def test_3(self):
        self.assertEqual(two_sum([3,3], 6), [0,1])

    def test_no_solution(self):
        self.assertIsNone(two_sum([1,2,3], 10))

    def test_empty(self):
        self.assertIsNone(two_sum([], 5))

if __name__ == "__main__":
    unittest.main()
