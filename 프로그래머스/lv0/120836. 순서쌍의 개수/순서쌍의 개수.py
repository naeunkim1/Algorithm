def solution(n):
    cnt = 0
    for i in range(1, n+1):
        if i*(n//i) == n:
            cnt += 1

    return cnt