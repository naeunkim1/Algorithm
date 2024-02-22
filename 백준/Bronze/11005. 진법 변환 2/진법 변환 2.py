N, B = map(int, input().split())
s = ''
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0

while N:
  s += str(number[N%B])
  N //= B

print(s[::-1])