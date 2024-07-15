from collections import deque

for tc in range(10):
    T = int(input())
    frame = [list(map(int,input())) for _ in range(100)]
    start_y = 0
    start_x = 0
    result = 0
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    q = deque()
    
    for i in range(100):
        for j in range(100):
            if frame[i][j] == 2:
                start_y, start_x = i,j
                q.append((start_y,start_x))
                break
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny, nx = y+direction[i][0], x+direction[i][1]
            if frame[ny][nx] == 3:
                result = 1
                break
            if 0<=nx<100 and 0<=ny<100 and frame[ny][nx] == 0:
                frame[ny][nx] = 1
                q.append((ny,nx))
    print("#{} {}".format(tc + 1, result))
    
            
            
            
            
