def solution(citations):
    
    result = 0
    length = len(citations)
    for i, x in enumerate(sorted(citations)):
        if x  >= length - i:
            result = max(result, length-i)
    return result