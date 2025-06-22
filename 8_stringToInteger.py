
def myAtoi(s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    
    negative = False
    if s[0] == "-":
        negative = True
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]
    ans = ""

    for item in s:
        if item.isdigit():
            ans += item
        else: break
    if ans == "":
        return 0 
    ans = -int(ans) if negative is True else int(ans)
    
    if ans > 2**31 -1:
        return 2**31 -1
    if ans < -2**31:
        return -2**31
    
    return ans


