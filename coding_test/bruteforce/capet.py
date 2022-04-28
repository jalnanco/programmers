def solution(brown, yellow):
    # a*b = brown + yellow
    sum = brown + yellow
    
    answer = []
    for x in range(sum):
        x += 1
        sumx = x
        sumy = sum/x        
        if(sumy.is_integer() and sumx >= sumy):
            if (sumx + sumy) * 2 - 4 == brown:
                answer = [sumx, sumy]
                break;
            
#             print(sumx, int(sumy))
#             print(sumx + sumx + sumy + sumy - 4 == brown)

    return answer