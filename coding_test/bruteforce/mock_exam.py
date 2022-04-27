def solution(answers):
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]    
    for i, z in enumerate(answers):
        if z == a[i % 5]:
            score[0] += 1
        if z == b[i % 8]:
            score[1] += 1
        if z == c[i % 10]:
            score[2] += 1

    answer = []
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)
    
    return answer