def solution(n, lost, reserve):
    count = 0
    for x in lost:
        if x in reserve:
            lost.remove(x)
            reserve.remove(x)
        
    for x in sorted(lost):
        if x > 1 and x-1 in reserve:
            reserve.remove(x-1)
            count +=1
        elif x in reserve:
            reserve.remove(x)
            count +=1
        elif x+1 in reserve:
            reserve.remove(x+1)
            count +=1
    return n - len(lost) + count