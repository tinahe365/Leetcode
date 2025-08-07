

def solution(arr, target):
    """
    Find any pair [x, y] in arr such that x + y == target.
    If multiple valid pairs exist, returns the one whose second element
    appears earliest in the array. If still tied, pairs with the earliest first element.
    If no such pair exists, returns [].
    """
    seen = {}  # value -> its earliest index
    for j, v in enumerate(arr):
        c = target - v
        if c in seen:
            return [c, v]
        # only record v the first time we see it
        if v not in seen:
            seen[v] = j

        print(f"Checking value: {v}, complement: {c}, seen: {seen}")
    return []

arr = [1, 2, 3, 4, 9, 10]
solution(arr, 13)  # Example usage, can be removed in production code
