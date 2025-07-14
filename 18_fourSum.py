from typing import List
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    if len(nums) < 4:
        return []

    nums.sort()
    output = []

    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            left = j + 1
            right = len(nums) - 1
            while left < right:
                
                four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if four_sum == target:
                    candidates = [nums[i], nums[j], nums[left], nums[right]]
                    if candidates not in output:
                        output.append(candidates)
                    left += 1
                    right -= 1
                elif four_sum < target:
                    left += 1
                else:
                    right -=1
                    
    return output


# Recursive version
def fourSum(nums: list[int], target: int):
    ans = []

    def nSum(
            l: int, r: int, target: int, n: int, path: list[int],
            ans: list[list[int]]) -> None:
      """Finds n numbers that add up to the target in [l, r]."""
      if r - l + 1 < n or n < 2 or target < nums[l] * n or target > nums[r] * n:
        return
      
      if n == 2:
        while l < r:
          summ = nums[l] + nums[r]
          if summ == target:
            ans.append(path + [nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l - 1] and l < r:
              l += 1
          elif summ < target:
            l += 1
          else:
            r -= 1
        return

      for i in range(l, r + 1):
        if i > l and nums[i] == nums[i - 1]:
          continue

        nSum(i + 1, r, target - nums[i], n - 1, path + [nums[i]], ans)

    nums.sort()
    nSum(0, len(nums) - 1, target, 4, [], ans)
    return ans