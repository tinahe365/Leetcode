class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = -1
        n1 = len(haystack)
        n2 = len(needle)
        find = True
        
        for i in range(n1):
            if i+n2 > n1:
                return output
            if haystack[i:(i+n2)] == needle: # compare as a whole
                return i
        
        return output
        