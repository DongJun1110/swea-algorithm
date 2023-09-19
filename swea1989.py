n = int(input())
for i in range(n):
  str = input()
  if str == str[::-1]:
    print('#{} {}'.format(i+1,1))
  else:
    print('#{} {}'.format(i+1,0))
    