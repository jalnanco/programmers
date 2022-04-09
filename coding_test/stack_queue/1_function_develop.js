function cacluate_hundred(a, speed, count) {
    a += count * speed
    while (a < 100) {
        a += speed
        count++
    }
    return count
}

function solution(progresses, speeds) {
    var answer = []
    var progress = 0
    
    count = 0
    progresses = progresses.map((x, i) => {
        count = cacluate_hundred(progresses[i], speeds[i], count)        
        return count
    })    
    
    z = 0
    index = -1
    progresses.forEach((a) => {
        if (a !== z) {
            answer.push(1)
            index += 1
            z = a
        } else {
            answer[index] += 1
        }
    })
    
    return answer;
}