t = int(input())
for tc in range(t):
  
  n = int(input())
  dist = [[0,1],[1,0],[0,-1],[-1,0]]
  arr = [[0 for _ in range(n)] for _ in range(n)]

  num = 1
  d = 0
  x,y = 0,-1
  
  while num <= n*n:
    xidx, yidx = x+dist[d][0], y+dist[d][1]
    if 0<=xidx<n and 0<=yidx<n and arr[xidx][yidx] == 0:
      arr[xidx][yidx] = num
      num += 1
      x,y = xidx, yidx

    else:
      d = (d+1) % 4

  print('#{}'.format(tc+1))

  for i in arr:
    print(*i)
  

  