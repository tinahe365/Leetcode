def maxFrequency(nums, k, numOperations):
        nums = sorted(nums)
        count, max_frequency, operations = 0, 0, 0
        pre_range = [float('-inf'), float('inf')]

       
        for i in range(0, len(nums)):
            cur_range = [nums[i] - k, nums[i] + k]
            if cur_range[0] <= pre_range[1] and operations < numOperations:
                count += 1
                operations += 1
                print(nums[i], count)
            else:
                max_frequency = max(max_frequency, count)
                count = 1
                operations = 0
            pre_range = cur_range
        return max(max_frequency, count)

nums = [23,54]
print(maxFrequency(nums, 77, 1))