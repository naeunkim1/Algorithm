def solution(brown, yellow):
    answer = []
    if int((-(4-brown)-((4-brown)**2-16*yellow)**0.5)/4) > 0:
        n = int((-(4-brown)-((4-brown)**2-16*yellow)**0.5)/4)
    else:
        n = int((-(4-brown)+((4-brown)**2-16*yellow)**0.5)/4)
    return [(yellow/n)+2, n+2]