from typing import List
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()

    n = len(nums)
    if target <= nums[0] + nums[1] + nums[2]:
        return nums[0] + nums[1] + nums[2]
    if target >= nums[n-1] + nums[n-2] + nums[n-3]:
        return nums[n-1] + nums[n-2] + nums[n-3]
    
    distance_points = {}
    d_min = max(abs(nums[n-1]) + abs(nums[n-2]) +abs(nums[n-3]) + abs(target), 
                abs(nums[0]) + abs(nums[1]) + abs(nums[2]) + abs(target))
    
    for i in range(len(nums)-2):
        left = i + 1
        right = n - 1
        print(f"i: {i}, nums[i]: {nums[i]}, left: {left}, right: {right}, d_min: {d_min}")    
        while left < right:
            
            threeSum =  nums[i] + nums[left] + nums[right]
            # if nums[i] == 9:
            #     print(f"9: i: {i}, left: {nums[left]}, right: {nums[right]}, threeSum: {threeSum}, target: {target}")
            if threeSum == target:
                return threeSum
            if abs(threeSum - target) < d_min:
           
                d_min =  abs(threeSum - target)
                distance_points[d_min] = threeSum
                #print(distance_points, nums[i], nums[left] , nums[right])

            if threeSum > target:
                right -= 1
            elif threeSum < target:
                left += 1
           
   
    if distance_points:
        threeSum = distance_points[min(distance_points.keys())]
        return threeSum
    

    # nums.sort()
    # output =  nums[0] + nums[1] + nums[2]
    # for i in range(0,len(nums)-2):
    #     for j in range(i+1,len(nums)-1):
    #         for k in range(j+1, len(nums)):
    #             threeSum = nums[i] + nums[j] + nums[k]
    #             if threeSum - target == 0:
    #                 return threeSum
    #             elif abs(threeSum - target) < abs(output - target):
    #                 output = threeSum

    # return output
    


# nums = [4,0,5,-5,3,3,0,-4,-5]
# print(threeSumClosest(nums, -2))  # Output: -2

# nums = [10,20,30,40,50,60,70,80,90]
# print(threeSumClosest(nums, 1))  

# nums = [2,3,8,9,10]
# print(threeSumClosest(nums, 16))  

print(threeSumClosest([-84,92,26,19,-7,9,42,-51,8,30,-100,-13,-38], 78))