tc = int(input())
for t in range(tc):
  li = list(map(int,input().split()))
  li.remove(min(li))
  li.remove(max(li))
  aver = sum(li)/8
  print('#{} {}'.format(t+1,round(aver)))
  
  
