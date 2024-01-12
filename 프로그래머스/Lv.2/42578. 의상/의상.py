def solution(clothes):
    answer = 1
    hashDict = {}
    for name, kind in clothes:
        if kind in hashDict.keys():
            hashDict[kind] += [name]
        else: 
            hashDict[kind] = [name]
    for _, value in hashDict.items():
        answer *= (len(value)+1)

    return answer-1