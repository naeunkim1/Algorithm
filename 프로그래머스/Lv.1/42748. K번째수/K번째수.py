def solution(array, commands):
    answer = []
    res = []
    for i in range(len(commands)):
        res = array[commands[i][0]-1:commands[i][1]]
        res.sort()
        answer.append(res[commands[i][-1]-1])
    return answer