A = []
for _ in range(9):
  A.append(list(map(int, input().split())))
max_num = -1
X = 0
Y = 0
for row in range(9):
  for col in range(9):
    if max_num < A[row][col]:
      max_num = A[row][col]
      X = row + 1
      Y = col + 1
print(max_num)
print(X, Y)