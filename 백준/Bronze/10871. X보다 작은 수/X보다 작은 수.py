import sys
N, X = sys.stdin.readline().split(" ")
A = list(map(int, input().split()))


for j in A:
    if j < int(X):
        print(j, end=" ")
