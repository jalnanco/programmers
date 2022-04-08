import collections
    
def solution(genres, plays):
    result = []
    answer = []
    counter = collections.Counter()
    for x, y in zip(genres, plays):
        counter.update({x:y})
    sorted_counter = sorted(counter.items(), key = lambda item: item[1], reverse=True)
    genre_order = dict(sorted_counter).keys()

    d = collections.defaultdict(list)
    for k, v in zip(genres, plays):
        d[k].append(v)
    for g in genre_order:
        result += sorted(d[g], reverse=True)[:2]
        for x in result:
            for i in range(len(genres)):
                if genres[i] == g and plays[i] == x and i not in answer:
                    answer.append(i)
    return answer