import collections

def solution(clothes):
    answer = 1
    d = collections.defaultdict(list)
    for v, k in clothes:
        d[k].append(v)
    for key in d.keys():
        answer = answer * (len(d[key]) + 1)
    return answer - 1