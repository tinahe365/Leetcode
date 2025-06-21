from typing import List
def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    ans0 = set(nums1)
    ans1 = set(nums2)
    
    # common_nums = ans0.intersection(ans1)

    # for item in common_nums:
    #     ans0.remove(item)
    #     ans1.remove(item)
    
    # return ([list(ans0),list(ans1)])

    return [list(ans0 - ans1), list(ans1 - ans0)] # This is a more concise way to find the difference



