def solution(numbers, target):
    x = [0]
    cnt = 0
    for num in numbers:
        tmp = []
        for i in x:
            tmp.append(i + num)
            tmp.append(i - num)
        x = tmp
    for i in x:
        if i == target:
            cnt+=1
    return cnt