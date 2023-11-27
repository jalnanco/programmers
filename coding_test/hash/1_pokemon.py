def solution(nums):
    maxSelectable =  len(nums) / 2
    uniq = len(set(nums))
    
    if maxSelectable <= uniq:
        return maxSelectable
    return uniq

# Other solution
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))