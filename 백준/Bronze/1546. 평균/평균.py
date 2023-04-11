N = int(input())
score = list(map(int, input().split()))
lst = [i/max(score)*100 for i in score]
print(sum(lst)/len(lst))