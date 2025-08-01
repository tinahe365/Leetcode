from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        # 1) find pivot
        for p in range(n-2, -1, -1):
            if nums[p] < nums[p+1]:
                print(f"Pivot found at index {p} with value {nums[p]}, next value {nums[p+1]}")
                break
        else:
            # no pivot -> highest permutation
            nums.reverse()
           
            return

        # 2) find successor
        for q in range(n-1, p, -1):
            if nums[q] > nums[p]:
                break

        # 3) swap pivot & successor
        nums[p], nums[q] = nums[q], nums[p]

        # 4) reverse the suffix
        nums[p+1:] = nums[p+1:][::-1]

solution = Solution()
nums = [4,2,0,2,3,2,0]
solution.nextPermutation(nums)
