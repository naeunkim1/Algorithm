def solution(emergency):
    answer = []
    x = sorted(emergency, reverse = True)
    
    for i in range(len(emergency)):
        answer.append(x.index(emergency[i])+1)
    return answer