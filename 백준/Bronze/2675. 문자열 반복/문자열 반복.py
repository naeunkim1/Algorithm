T= int(input())
for _ in range(T):
  x = ''
  R, S = map(str, input().split())
  for y in S:
    x += y*int(R)
  print(x)