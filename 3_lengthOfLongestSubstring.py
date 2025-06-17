def lenghthOfLongestSubstring(s:str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    
    :param s: Input string
    :return: Length of the longest substring without repeating characters
    """
    char_index_map = {} 
    left = 0
    max_length = 0

    for right in range(len(s)):
        print(char_index_map, left)
        if s[right] in char_index_map:
            left = max(left, char_index_map[s[right]] + 1)
        char_index_map[s[right]] = right
      
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    # Example usage:
    # s = "au"
    # result = lenghthOfLongestSubstring(s)
    # print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")
    
    # s = "bbbbb"
    # result = lenghthOfLongestSubstring(s)
    # print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")
    
    # s = "pwwkew"
    # result = lenghthOfLongestSubstring(s)
    # print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")

    s = "dvdf"
    result = lenghthOfLongestSubstring(s)
    print(f"The length of the longest substring without repeating characters in '{s}' is: {result}")