def generateParentheses(n):
    path, result = [], []
    def backtrack(left, right):
        print(f"backtrack called with left: {left}, right: {right}, path: {path}")
        if left == n and right == n:
            result.append("".join(path))
            return
        if left < n:
            path.append('(')
            print(f"Added '(' to path: {path}")
            backtrack(left + 1, right)
            print(f"Backtracked after adding '(' and before pop {path}")
            path.pop()
            print(f"Backtracked after adding '(' and after pop {path}")
        if right < left:
            path.append(')')
            print(f"Added ')' to path: {path}")
            backtrack(left, right + 1)
            print(f"Backtracked after adding ')' and before pop {path}")
            path.pop()
            print(f"Backtracked after adding ')' and after pop {path}")
    backtrack(0, 0)
    return result

generateParentheses(3)