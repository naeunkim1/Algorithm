def solution(nums):
    x = len(set(nums))
    
    if len(nums) // 2 >= x : return x
    else : return len(nums) // 2