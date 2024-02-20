words = []
length = []
for _ in range(5):
  word = input()
  words.append(word)
  length.append(len(word))

result = ''
for j in range(max(length)):
  for i in range(5):
    if j < length[i]:
      result += words[i][j]
print(result)