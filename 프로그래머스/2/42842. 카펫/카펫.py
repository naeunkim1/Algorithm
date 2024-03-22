def solution(brown, yellow):
    b = (brown-4)//2
    y = yellow
    return [(b+(b**2-4*y)**0.5)//2+2, (b-(b**2-4*y)**0.5)//2+2]