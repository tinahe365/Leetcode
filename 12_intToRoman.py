class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""

        for i in range(0,len(str(num))):
            current_digit = (num // 10**i) % 10
            match i:
                case 0:
                    one, five, nine = "I", "V", "IX"
                case 1:
                    one, five, nine = "X", "L", "XC"
                case 2:
                    one, five, nine = "C", "D", "CM"
                case 3:
                    one, five, nine = "M", "" , ""

            int_roman_map = {
                0 : "",
                1 : one,
                2 : one + one,
                3 : one + one + one,
                4 : one + five,
                5 : five,
                6 : five + one,
                7 : five +  one + one,
                8 : five + one + one + one,
                9 : nine
            }
            output = int_roman_map[current_digit] + output

        return output