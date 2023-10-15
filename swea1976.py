for tc in range(int(input())):
  
  li = list(map(int,input().split()))
  hour = li[0] + li[2]
  min = li[1] + li[3]

  if min > 59:
    min -= 60
    hour += 1

  if hour > 12:
    hour -= 12

  print('#{} {} {}'.format(tc+1,hour,min))