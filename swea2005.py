T = int(input())
for tc in range(T):
  
    N = int(input())
    totalArr = []
    for i in range(N):
      oneLineArr = []
      for j in range(i+1):
        if j == 0 or j == i:
          oneLineArr.append(1)
        else:
          oneLineArr.append(totalArr[i-1][j-1]+totalArr[i-1][j])
      totalArr.append(oneLineArr)

    print('#{}'.format(tc))
    for i in totalArr:
      print(*i)