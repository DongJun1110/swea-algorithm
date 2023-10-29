t = int(input())

for tc in range(t):
  n = int(input())
  change = [0] * 8
  money = [50000,10000,5000,1000,500,100,50,10]
  for i in range(8):
    if n // money[i] != 0:
      change[i] = n//money[i]
      n = n%money[i]
  
  print('#{}'.format(tc+1))
  print(*change)