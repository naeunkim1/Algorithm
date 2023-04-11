num = [i+1 for i in range(30)]
lst1 = [int(input()) for j in range(28)]
lst2 = [k for k in num if k not in lst1]
print(min(lst2))
print(max(lst2))