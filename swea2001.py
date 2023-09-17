t = int(input())
for tc in range(t):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    maxKill = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly = 0
            for k in range(m):
                for l in range(m):
                    fly += arr[k+i][l+j]
            maxKill = fly if fly > maxKill else maxKill
    print('#{} {}'.format(tc+1,maxKill))