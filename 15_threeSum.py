from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:

    for i, a in enumerate(nums):
        print(f"i: {i}, a: {a}")

nums = [-1, 0, 1, 2, -1, -4]
threeSum(nums)