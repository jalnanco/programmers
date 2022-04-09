def solution(prices):
    res = [0 for x in range(len(prices))]
    for i, x in enumerate(prices):
        # 리스트 인덱스 슬라이싱 사용 시 효율성 테스트 떨어짐
        # for y in prices[i+1:]:
        #     res[i] += 1
        #     if x > y:
        #         break
        for y in range(i+1,len(prices)):
            res[i] += 1
            if x > prices[y]:
                break
    return res