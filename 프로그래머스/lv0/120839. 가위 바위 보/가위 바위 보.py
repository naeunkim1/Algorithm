def solution(rsp):
    r = {'2':'0', '0':'5', '5':'2'}
    answer = ''
    for i in rsp:
        answer+=r[i]
    return answer