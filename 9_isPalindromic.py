def isPalindrome(x: int) -> bool:
    if x>= 0:
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
    return False