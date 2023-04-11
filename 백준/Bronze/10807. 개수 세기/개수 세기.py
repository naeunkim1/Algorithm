N = int(input())
A = input().split()
v = int(input())
cnt = 0
for i in range(N):
  if int(A[i]) == v: cnt+=1
print(cnt)