import heapq

def solution(jobs):
    
    cur, total = 0, 0
    working = []
    length = len(jobs)
    tasks = sorted([(x[1], x[0]) for x in jobs],
                   key=lambda x: (x[1], x[0]), reverse=True)
    while tasks or working:
        while len(tasks) > 0 and tasks[-1][1] <= cur:
            heapq.heappush(working, tasks.pop())
        if not working:
            heapq.heappush(working, tasks.pop())
        w = heapq.heappop(working)
        
        if cur < w[1]:
            cur = w[1]
        total += cur - w[1] + w[0]
        cur += w[0]
            
    return total//length