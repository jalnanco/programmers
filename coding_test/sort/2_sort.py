def solution(numbers):
    
    z = [ ((str(x)*4)[:4], x) for x in numbers ]
    
    answer = ""
    for x in sorted(z, reverse=True):
        answer += str(x[1])
        
    if answer[0] == "0":
        return "0"
        
    return answer