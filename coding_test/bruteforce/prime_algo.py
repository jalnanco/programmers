def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True

def dfs(result, complete, choose, others):
    complete = complete + str(choose)
    if is_prime(int(complete)):
        result.add(int(complete))

    # print (result, "C:",complete, "C:",choose, "O:",others)    
    if len(others) == 1:
        complete = complete + str(others)
        if is_prime(int(complete)):
            result.add(int(complete))
    else:
        for i, x in enumerate(others):
            dfs(result, complete, others[i], others[i+1:] + others[:i])


def solution(numbers):
    result = set()
    
    for i, x in enumerate(numbers):
        dfs(result, "", numbers[i], numbers[i+1:] + numbers[:i])
            
    print(result)
    return len(result)