def solution(array, commands):
        res = []
    for com in commands:
        i, j, k = com
        print(i,j,k)
        arr = sorted(array[i-1:j])
        res.append(arr[k-1])    
    return res