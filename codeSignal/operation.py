def solution(queries):
    container = []
    output = []
    
    for item in queries:
        if item[0] == "ADD":
            container.append(item[1])
            output.append("")
        elif item[0] == "EXISTS" or item[0] == "REMOVE":
            exist = "true" if item[1] in container else "false"
            output.append(exist)
            if item[0] == "REMOVE" and exist == "true":
                container.remove(item[1])
        elif item[0] == "GET_NEXT":
            # digit_container = set(container)
            # digit_container.discard("")
            # digit_container.discard("true")
            # digit_container.discard("false")
            digit_container = set(container) - {"", "true", "false"}
            
            transposed_digit = map(lambda x: int(x),list(digit_container)) 
            sorted_digits = sorted(transposed_digit)
            
            for i in sorted_digits:
                if i > int(item[1]):
                    container.append(str(i))
                    output.append(str(i))
                    break
                if i == sorted_digits[-1] and i <= int(item[1]):
                    output.append("")
                      
    
    return output
            
            
queries = [
    ["ADD","1"], 
    ["ADD","2"], 
    ["ADD","2"], 
    ["ADD","4"], 
    ["GET_NEXT","1"], 
    ["GET_NEXT","2"], 
    ["GET_NEXT","3"], 
    ["GET_NEXT","4"], 
    ["REMOVE","2"], 
    ["GET_NEXT","1"], 
    ["GET_NEXT","2"], 
    ["GET_NEXT","3"], 
    ["GET_NEXT","4"]]
print(solution(queries))