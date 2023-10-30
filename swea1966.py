t = int(input())
for tc in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    li.sort()
    print('#{}'.format(tc+1),end = ' ')
    print(*li)
