import heapq

heap, max_heap = [], []
heapq.heapify(heap)
heapq.heapify(max_heap)

def solution(operations):
    
    # 가설) 최대값과 최소값을 힙 안에 넣는다. 최소인지, 최대인지 표시
    # pop을 해서 최대나 최소가 나올때까지 뽑아서 제거한다.
    # 잘못나온 값은 도로 넣는다.
    
    # 가설2) 최대값으로 정렬된 값과 최소값으로 정렬된 값 2개를 만든다.
    # 최대값이나 최소값에 빠질때 같이 뺀다.
    for x in operations:
        a, b = x.split(" ")
        b = int(b)
        if a == "I":
            heapq.heappush(heap, b)
            heapq.heappush(max_heap, -b)
            print ("INSERT:", b, heap, max_heap)
        if heap and a == "D":
            if b == 1:
                t = heapq.heappop(max_heap)
                heap.remove(-t)
                heapq.heapify(heap)
            if b == -1:
                t = heapq.heappop(heap)
                max_heap.remove(-t)
                heapq.heapify(max_heap)
            print ("DELETE:", t, heap, max_heap)

    answer = [0, 0];
    if heap:
        answer[1] = heapq.heappop(heap)
    if max_heap:
        answer[0] = -heapq.heappop(max_heap)
        
    return answer