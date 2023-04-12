alpa = input().upper()
words = list(set(alpa))

lst = []
for i in words :
  lst.append(alpa.count(i))
if lst.count(max(lst)) > 1: 
  print("?")
else:
  print(words[lst.index(max(lst))])