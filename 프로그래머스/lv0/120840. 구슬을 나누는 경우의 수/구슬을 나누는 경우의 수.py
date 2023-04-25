def pact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def solution(balls, share):
    return pact(balls)/(pact(balls-share)*pact(share))