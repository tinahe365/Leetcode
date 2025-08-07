import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import unittest
from solution import solution


class UnitTests(unittest.TestCase):
    def test_01(self):
        arr = [1, 2, 3, 4, 9, 10]
        T = 13
        expected_result = [4, 9]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_02(self):
        arr = arr = [i for i in range(1,501)]
        T = 629
        expected_result = [314, 315]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_03(self):
        arr = [50, -50]
        T = 100
        expected_result = []
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_04(self):
        arr = [0, 0, 0, 0, 0]
        T = 0
        expected_result = [0, 0]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_05(self):
        arr = [-100, -50, 0, 50, 100]
        T = -150
        expected_result = [-100, -50]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_06(self):
        arr = [-66, 45, 95, -84, -35, -70, 26, 94, 15, 20, 66, -3, -47, -76, 24, -93, -1, 10, 55, 95, 96, -100, 78, 14, -32, 84, -42, 51, -74, -19, -93, -95, -94, 66, 38, -98, -3, 75, -45, 8, 85, -93, 35, -44, 95, 12, 26, 41, -41, -12, -41, 73, -44, 94, 17, -26, -95, 6, 42, 64, -75, -53, 61, 85, -25, -70, 90, -15, 84, 82, 28, 8, 29, 71, -52, -23, -28, 50, 27, 29, 0, 50, -92, 22, -38, 90, 3, 6, 70, -56, -7, 40, 79, 98, 72, 88, -5, -78, 12, 69]
        T = -10
        expected_result = [66, -76]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_07(self):
        arr = [100] * 500
        T = 200
        expected_result = [100, 100]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_08(self):
        arr = [-100] * 500
        T = -200
        expected_result = [-100, -100]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)

    def test_09(self):
        arr = list(range(1000000))
        T = 1215634
        expected_result = [607816, 607818]
        result = solution(arr, T)
        self.assertEqual(result, expected_result)
