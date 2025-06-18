def findMedianSortedArrays(nums1, nums2):
    i, j = 0, 0
    m, n = len(nums1), len(nums2)
    nums3 = []
    x = (m + n) // 2
    
    # if m == 0 and n == 0:
    #     return ""
    for _ in range(x+1):
        if i == m:
            nums3 += nums2[j:]
        elif j == n:
            nums3 += nums1[i:]
        else:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                nums3.append(nums1[i])
                nums3.append(nums2[j])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                nums3.append(nums2[j])
                j += 1

    if (m + n) / 2 > x:
        return nums3[x]
    else:
        return (nums3[x-1]+nums3[x])/2
    

def refactoredFindMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total = m + n
    mid = total // 2
    is_even = (total % 2 == 0)

    i, j = 0, 0
    curr = prev = 0
    for _ in range(mid + 1):
        prev = curr
        if i < m and (j >= n or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    return curr if not is_even else (prev + curr) / 2

if __name__ == "__main__":
    # Example usage:
    nums1 = [1, 3]
    nums2 = [2]
    print(f"The median of {nums1} and {nums2} is: {findMedianSortedArrays(nums1, nums2)}")
    
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(f"The median of {nums1} and {nums2} is: {findMedianSortedArrays(nums1, nums2)}")
    
    nums1 = [0, 0]
    nums2 = [0, 0]
    print(f"The median of {nums1} and {nums2} is: {findMedianSortedArrays(nums1, nums2)}")
    
    nums1 = []
    nums2 = [1]
    print(f"The median of {nums1} and {nums2} is: {findMedianSortedArrays(nums1, nums2)}")
    
    # nums1 = []
    # nums2 = []
    # print(f"The median of {nums1} and {nums2} is: {findMedianSortedArrays(nums1, nums2)}")
    
  
    print(f"Refactored median of {nums1} and {nums2} is: {refactoredFindMedianSortedArrays(nums1, nums2)}")