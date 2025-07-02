class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
            "I":1, "V":5, "X":10, 
            "L":50, "C":100, "D":500,
            "M":1000
        }
        
        pre_num, current_num, ans = 0,0,0
        for item in s:
            current_num = roman_int_map[item]
            ans += current_num
            if current_num > pre_num:
                ans -= 2 * pre_num
            pre_num = current_num

        return ans
            

        
   
