from heapq import heapify, heappush, heappop

def solution(scoville, K):
    
    heap = []
    heapify(heap)
    
    for x in scoville:
        heappush(heap, x)
        
    count = 0
    while heap[0] <= K:
        if len(heap) == 1:
            return -1
        count += 1
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, a + (b * 2))
    
    # 순회 시 효율성 실패

    # while min(scoville) < K:
    #     if len(scoville) == 1:
    #         return -1
    #     min1 = min(scoville)
    #     scoville.remove(min1)
    #     min2 = min(scoville)
    #     scoville.remove(min2)
    #     scoville.append(min1 + (min2 * 2))
    #     count += 1
    
    return count