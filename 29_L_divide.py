class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n, output = 0, 0
        if dividend == 0:
            return 0

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sameSign = True
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sameSign = False
        
        d, dv = abs(dividend), abs(divisor)
    

        while d >= dv:
            temp = dv
            mul = 1

            while d >= temp:
                d -= temp
                output += mul
                mul += mul
                temp += temp
                
        if sameSign:
            return min(2**31-1, output)
        else:
            return max(-2**31, -output)
            