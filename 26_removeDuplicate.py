class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        
        for index in range(0,len(nums)):
            if nums[index] == nums[unique-1]:
                continue
            else:
                nums[unique] = nums[index]
                unique += 1
            
        return unique
                