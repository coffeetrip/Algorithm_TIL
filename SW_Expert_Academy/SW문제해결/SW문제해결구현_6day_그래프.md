### 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

```python
def bfs(start, goal):
    queue = [0]*(1000000)
    visited = [0]*(1000000 + 1)
    push_idx = -1
    pop_idx = -1

    push_idx += 1
    queue[push_idx] = start
    visited[start] = 1

    if start == goal:
        return 0

    while push_idx != pop_idx:
        pop_idx += 1
        x = queue[pop_idx]

        for nx in [x+1, x-1, 2*x, x-10]:
            if visited[nx] == 0 and 0 < nx <= 1000000:
                visited[nx] += visited[x] + 1
                push_idx += 1
                queue[push_idx] = nx

                if nx == goal:
                    return visited[nx] - 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}' .format(tc, bfs(N, M)))
```

