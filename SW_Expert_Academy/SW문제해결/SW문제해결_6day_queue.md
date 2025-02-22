## 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

```python
for tc in range(int(input())):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    while m > 0:
        num.append(num.pop(0))
        m -= 1
    print(f'#{tc+1} {num[0]}')
```



## 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

```python
def bfs(i, j, N):
    global maze
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 초기화
    q = []    # 큐생성
    visited = [[0 for _ in range(N)] for _ in range(N)]  # visited 생성
    q.append([i, j])  # 시작점 인큐
    visited[i][j] = 1  # 시작점 방문표시

    # 탐색
    while len(q) != 0:  # 큐가 비어있지 않으면 반복
        n = q.pop(0)  # 디큐
        i, j = n[0], n[1]
        if maze[i][j] == 3:  # visit()
            return visited[i][j] - 2
        # i, j 에 인접하고 방문하지 않은 칸을 인큐
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<N and nj>=0 and nj<N:   # 미로를 벗어나지 않았고
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 벽이 아니고, 방문하지 않은 칸이면
                    q.append([ni, nj])  # 인큐
                    visited[ni][nj] = visited[i][j] + 1  # 방문표시
    return 0

for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                startI = i
                startJ = j
    print(f'#{tc+1} {bfs(startI, startJ, N)}')
```

