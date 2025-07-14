def letterCombinations(digits: str) -> list[str]:
    num_letters_map = {
        "2":"abc", "3":"def",
        "4":"ghi", "5":"jkl",
        "6":"mno", "7":"pqrs",
        "8":"tuv", "9":"wxyz"
    }
    output, new_output = [],[]
   
    for digit in digits:
        if not output:
            for letter in num_letters_map[digit]:
                output.append(letter)
        else:
            for item in output:
                for letter in num_letters_map[digit]:
                    new_output.append(item + letter)
            output = new_output
            new_output = []            
        
    return output

print(letterCombinations("234"))  # Example usage


# recursive version
from typing import List
def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            for letter in phone_map[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    output = []
    backtrack("", digits)
    return output