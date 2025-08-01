
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open_position = []
        start_point = -1
        max_count, count = 0,0
        # if len(s) <= 1:
        #     return 0
        
        for i in range(len(s)):
            if s[i] == "(":
                open_position.append(i)
    
            elif s[i] == ")":
                if not open_position: # no opened "("" in the array
                    count = 0
                    start_point = i
                else:
                    open_position.pop()
                    if open_position:
                        count = i - max(open_position[-1], start_point)
                    else:
                        count = i - start_point
                    
                    max_count = max(max_count, count)

        
                   
        return max_count
                


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        last_invalid = -1
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_length = max(max_length, i - stack[-1])
                    else:
                        max_length = max(max_length, i - last_invalid)
                else:
                    last_invalid = i
        
        return max_length