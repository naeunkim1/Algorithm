C = int(input())
for _ in range(C):
  N = list(map(int, input().split()))
  aver = sum(N[1:])/N[0]
  cnt = 0
  for i in range(1, len(N)):
    if N[i] > aver:
      cnt += 1
  print(str("{:.3f}".format(cnt/N[0]*100))+'%')