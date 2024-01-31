for t in range(int(input())):
  n,m = map(int,input().split())
  nstr = list(map(str,input().split()))
  mstr = list(map(str,input().split()))
  qyear = []
  for q in range(int(input())):
    qyear.append(int(input()))

  print('#{}'.format(t+1),end=' ')
  for year in qyear:
    first = year%len(nstr)
    second = year%len(mstr)
    print(nstr[first-1]+mstr[second-1],end=' ')
  print()
    
    
  
  
  

