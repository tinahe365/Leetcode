
def isMatch(s: str, p: str) -> bool:
    pointer_s, pointer_p = 0, 0
    while pointer_s < len(s) and pointer_p < len(p):
        if s[pointer_s] == p[pointer_p]:
            pointer_s += 1
            pointer_p += 1
        elif p[pointer_p] == ".":
            pointer_s += 1
            pointer_p += 1
        elif p[pointer_p] == "*":
            if s[pointer_s] == p[pointer_p-1] or p[pointer_p-1] == ".": # pointer_s matches with p* (0 or more times)
               
                pointer_s +=1
                print("same as previouse", pointer_s, pointer_p)
            else: # s does not match with p*
                print("not same as previouse", pointer_s, pointer_p)
                pointer_p += 1
                
            if (pointer_s < len(s) and pointer_p < len(p)-1 and p[pointer_p + 1] == s[pointer_s]):
                pointer_p += 1
            
        else:
            pointer_p += 1
        print(pointer_s,pointer_p)
    return True if (pointer_s == len(s) and pointer_p == len(p)) else False

# s = "mississippi"
# p ="mis*is*ip*."
# print(isMatch(s, p))  # Should return True

# s = "aaa"
# p = "a*a"
# print(isMatch(s, p))  # Should return True

# s = "aaa"
# p = "ab*a"
# print(isMatch(s, p))  # Should return False

s = "aaa"
p = "ab*a*c*a"
print(isMatch(s, p))  # Should return True
