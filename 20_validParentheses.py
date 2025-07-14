def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    valid_parentheses = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    parentheses = []
    for item in s:
        if item in ['(','{','[']:
            parentheses.append(item)
        elif parentheses and valid_parentheses[item] == parentheses[-1]:
            parentheses.pop()
        else:
            return False
        
    return True if not parentheses else False