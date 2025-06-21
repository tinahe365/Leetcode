def longestPalindromicSubstring(s: str) -> str:
    def expand_around_center(left:int, right:int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(i,i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        # Even length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest
if __name__ == "__main__":
    # Example usage:
    s = "babad"
    result = longestPalindromicSubstring(s)
    print(f"The longest palindromic substring in '{s}' is: {result}")
    
    s = "cbbd"
    result = longestPalindromicSubstring(s)
    print(f"The longest palindromic substring in '{s}' is: {result}")
    
    s = "a"
    result = longestPalindromicSubstring(s)
    print(f"The longest palindromic substring in '{s}' is: {result}")
    
    s = "ac"
    result = longestPalindromicSubstring(s)
    print(f"The longest palindromic substring in '{s}' is: {result}")