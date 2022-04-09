def solution(priorities, location):
    
    ziped = [(x,y) for x, y in enumerate(priorities)]
    
    printed = []
    
    while len(ziped) != 0:
        a = [x[1] for x in ziped];
        b = ziped.pop(0)
        
        if max(a) == b[1]:
            printed.append(b)
        else:
            ziped.append(b)

    for i, z in enumerate(printed):
        if z[0] == location:
            return i+1
    answer = 0
    return answer