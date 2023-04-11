lst = []
for i in range(9):
  n = int(input())
  lst.append(n)
print(max(lst))
for i in range(9):
  if lst[i] == max(lst):
    print(i+1)