function solution(participant, completion) {
    var answer = '';
    
    participant.sort()
    completion.sort()
    answer = participant.filter((n, i) => n != completion[i])
        
    return answer[0];
}