from typing import List
def divideArray(nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    output = []
    if n <= 2:
        return []
    for i in range(2,n,3):
        current_array = []
        if nums[i] - nums[i-2] <= k:
            current_array = nums[i-2:i+1]
        else:
            return []
        output.append(current_array)

    return output

print(divideArray([1,3,4,8,7,9,3,5,1], 2))