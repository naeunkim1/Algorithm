def solution(clothes):
    hashDict = {}
    answer = 1
    
    for name, kind in clothes:
        if kind in hashDict.keys():
            hashDict[kind] += [name]
        else:
            hashDict[kind] = [name]
    for _, value in hashDict.items():
        answer *= (len(value)+1)

    return answer - 1