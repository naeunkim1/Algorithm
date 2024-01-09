def solution(progresses, speeds):
    answer = []
    days = []
    cnt = 0
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append((100 - progresses[i]) // speeds[i] + 1)
    for j in range(len(days)):
        if days[cnt] < days[j]:
            answer.append(j-cnt)
            cnt = j
            
    answer.append(len(days) - cnt)
            
    return answer