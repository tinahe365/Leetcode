from typing import List
def searchRange(nums: List[int], target: int) -> List[int]:
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            print(f"Left: {left}, Right: {right}, Mid: {mid}, Value: {nums[mid] if mid < len(nums) else 'N/A'}")
        return left

    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = findLeft(nums, target)
    right_index = findRight(nums, target)

    if left_index <= right_index and left_index < len(nums) and nums[left_index] == target:
        return [left_index, right_index]
    else:
        return [-1, -1]
    
# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # Output: [3, 4]