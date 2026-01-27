from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Count row occurrences by converting to tuples
        row_count = Counter(tuple(row) for row in grid)
        
        # Transpose grid using zip and count column occurrences
        col_count = Counter(tuple(col) for col in zip(*grid))
        
        # Sum up matches: for each row that exists as a column, 
        # multiply their occurrence counts
        return sum(row_count[row] * col_count[row] for row in row_count if row in col_count)

if __name__ == "__main__":
    solution = Solution()
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    result = solution.equalPairs(grid)
    print(result)  # Output: 1