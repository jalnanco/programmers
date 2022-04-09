function solution(priorities, location) {
    
    count = 0
    pair = priorities.map((x, i) => [x,i] )
    
    while (pair.length != 0) {
        x = pair.shift()
        if (x[0] < Math.max(...pair.map(x => x[0]))) {
            pair.push(x)
        } else {
            count += 1
            if (x[1] === location)
                return count
        }
    }
    
    var answer = 0;
    return answer;
}