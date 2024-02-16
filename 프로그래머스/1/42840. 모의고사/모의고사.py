def solution(answers):
    lst1 = [1,2,3,4,5]
    lst2 = [2,1,2,3,2,4,2,5]
    lst3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == lst1[idx%len(lst1)]:
            score[0] += 1
        if answer == lst2[idx%len(lst2)]:
            score[1] += 1
        if answer == lst3[idx%len(lst3)]:
            score[2] += 1
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
    return result