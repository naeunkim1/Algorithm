def solution(nums):
    x = len(nums) // 2
    numlst = list(set(nums))
    if x > len(numlst) :
        return len(numlst)
    return x