def solution(age):
    answer = [chr(i) for i in range(97, 107)]
    age = str(age)
    return ''.join(answer[int(age[i])] for i in range(len(age)))