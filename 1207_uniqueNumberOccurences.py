from typing import List
def uniqueOccurrences(arr: List[int]) -> bool:

    arr.sort()
    nuiqueNums = set(arr)

    occurrences = []

    for item in nuiqueNums:
        
        occurrences.append(arr.count(item))

    return True if len(occurrences) == len(set(occurrences)) else False

def refactoredUniqueOccurrences(arr: List[int]) -> bool:
    from collections import Counter

    count = Counter(arr)
    print(count)
    
    return len(list(count.keys())) == len(set(count.values()))
           
arr = [1,2,2,1,1,3]
arr = [1,2]


print(uniqueOccurrences(arr))  # Output: True
print(refactoredUniqueOccurrences(arr))  # Output: True