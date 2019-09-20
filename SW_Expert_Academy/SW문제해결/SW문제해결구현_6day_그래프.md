### 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

```python
def bfs(start, goal):
    global cnt
    q = [0]*1000000
    push = -1
    pop = -1
    visited = [0]*(1000000+1)

    push += 1
    q[push] = start
    visited[start] = 1

    if start == goal:
        return 0

    while push != pop:
        pop += 1
        x = q[pop]
        for nx in [x+1, x-1, 2*x, x-10]:
            if 0 < nx <= 1000000 and visited[nx] == 0:
                visited[nx] += visited[x] + 1
                push += 1
                q[push] = nx

                if nx == goal:
                    return visited[nx] -1

    return 0



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())


    print('#{} {}' .format(tc, bfs(N, M)))
```

