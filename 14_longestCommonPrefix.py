def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            # Shorten the prefix until it matches the start of the string
            prefix = prefix[:-1]
    
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))  # Output: "fl"

print(strs[0][:10])
