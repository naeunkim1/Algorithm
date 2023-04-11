N, M = map(int, input().split())
b = list(map(int, range(1, N+1)))
for x in range(M):
  i, j = map(int, input().split())
  k = 0
  k = b[i-1]
  b[i-1] = b[j-1]
  b[j-1] = k
for n in b:
  print(n, end=' ')