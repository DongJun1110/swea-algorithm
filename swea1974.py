for tc in range(int(int(input()))):
  li = [list(map(int,input().split())) for _ in range(9)]
  result = 1
  
  for i in range(9):
    arr_hor = [0] * 10
    arr_ver = [0] * 10
    for j in range(9):
      arr_hor[li[i][j]] = 1
      arr_ver[li[j][i]] = 1
  
    if arr_hor.count(0) >= 2 or arr_ver.count(0) >= 2:
      result = 0 
      break
  
  for k in range(3):
    arr_sqr = [0]*10
    for l in range(3):
      arr_sqr[li[l][k*3]] = 1
      arr_sqr[li[l][k*3+1]] = 1
      arr_sqr[li[l][k*3+2]] = 1
    if arr_sqr.count(0) >= 2:
      result = 0
      break
  
  print('#{} {}'.format(tc+1, result))
  