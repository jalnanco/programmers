function solution(nums) {
    const maxSelectable = nums.length / 2
    const uniqSet = new Set(nums)
    const uniqSize = uniqSet.size
    return maxSelectable <= uniqSize ?
        maxSelectable : uniqSize
}