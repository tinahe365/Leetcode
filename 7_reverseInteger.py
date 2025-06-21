
def reverse(x: int) -> int:
    is_negative = False
    if x == 0:
        return 0

    # while x % 10 == 0:
    #     x //= 10 # unnecessary, because int('00001') == 1
    
    if x < 0:
        is_negative = True
        x *= -1

    x_str = str(x)
    ans = ""

    # for i in range(len(x_str)-1, -1, -1):
    #     ans += x_str[i]
    ans = x_str[::-1] # more concise than the above loop
        
    ans = -int(ans) if is_negative else int(ans)
    if ans < -2**31 or ans > 2**31:
        return 0
    
    return ans


#  a solution from Leetcode, it's more concise and advanced than mine
    # a = str(x)
    # if x < 0:
    #     a = a[1::]
    #     print(a)
    #     a += '-' # smart, put the minus sign at the end
    # a = int(a[::-1]) 
    # print("Reversed integer:", a)
    # if -2**31 <= a <= 2**31-1:
    #     return a
    # return 0

x = -123
print(reverse(x))  # Output: 321


        