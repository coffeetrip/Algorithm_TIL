### 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

```
# i, j칸 까지 도착하는 최소 비용의 합

for i in range(1, N):
    for j in range(1, N):
        d[i][j] = min(d[i-1][j], d[i][j-1]) + arr[i][j]
```

```python
def f(i, j, total):
    global N, minV

    if minV < total:
        return
    if i == N-1 and j == N-1:
        if minV > total:
            minV = total
        return
    else:
        if 0 <= i+1 < N:
            f(i+1, j, total + array[i+1][j])
        if 0 <= j+1 < N:
            f(i, j+1, total + array[i][j+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    minV = 1000000000
    f(0, 0, array[0][0])

    print('#{} {}' .format(tc, minV))
```

```python
def f(i, j, total):
    global array, N, minV
    di = [0, 1]
    dj = [1, 0]

    if [i, j] == [N-1, N-1]:
        if minV > total:
            minV = total
    elif minV < total:
        return
    else:
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                f(ni, nj, total + array[ni][nj])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    minV = 10000000000
    f(0, 0, array[0][0])

    print('#{} {}' .format(tc, minV))
```



```python
def f(i, j, total ):
    global arr, to

    di = [0, 1]
    dj = [1, 0]

    total += arr[i][j]
    if len(to) >= 1 and to[-1] <= total:
        return 

    if (i, j) == (N-1, N-1):
        to.append(total)

    else:
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                f(ni, nj, total)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    to = []
    f(0, 0, 0)
    
    print('#{} {}' .format(tc, min(to)))
```

```python
# 혁준님
def DFS(i, j, total):
    global board
    global N
    global minV

    if [i, j] == [N - 1, N - 1]:
        if total < minV:
            minV = total
    else:
        if total < minV:
            d = [(1, 0), (0, 1)]

            for dx, dy in d:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < N and 0 <= nj < N:
                    DFS(ni, nj, total + board[ni][nj])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    minV = 10 * (2 * N - 1)

    DFS(0, 0, board[0][0])

    print("#{} {}".format(tc, minV))
```

```python
# 은지님
def f(i, j, p):
    global res

    if i == n-1 and j == n-1:
        res = min(p, res)
    elif p > res:
        return
    else:
        for x, y in ((0,1), (1,0)):
            ni, nj = i+x, j+y
            if 0<=ni<n and 0<=nj<n:
                f(ni, nj, p+arr[ni][nj])

for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 10*n*n
    f(0, 0, arr[0][0])
    print('#{} {}'.format(t, res))
```







### 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

```python
def battery(n, k):
    global minV

    if n == k:
        new = [0] + permutation + [0]
        min_battery = 0
        for i in range(len(new)-1):
            if min_battery > minV:
                return
            min_battery += golf_course[new[i]][new[i+1]]
        if minV > min_battery:
            minV = min_battery
    else:
        for i in range(n, k):
            permutation[i], permutation[n] = permutation[n], permutation[i]
            battery(n+1, k)
            permutation[i], permutation[n] = permutation[n], permutation[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    golf_course = [list(map(int, input().split())) for _ in range(N)]

    permutation = [i for i in range(1, N)]
    #permutation = list(range(1, N))

    minV = 100000000
    battery(0, N-1)
    print('#{} {}' .format(tc, minV))
```

```python
def f(n, s):
    global arr, visited, minV, N
    if not sum(visited):
        if minV > s + arr[n][0]:
            minV = s + arr[n][0]
    else:
        for i in range(1, N):
            if visited[i]:
                visited[i] = 0
                f(i, s + arr[n][i])
                visited[i] = 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 10000
    
    visited = [0] + [1] * (N - 1)
    f(0, 0)
    print("#{} {}".format(tc, minV))
```

```python
def f(n, k, s):
    global minV
    if n == k:
        if s + golf[p[-2]][p[-1]] < minV:
            minV = s + golf[p[-2]][p[-1]]
        return
    elif s > minV:
        return
    else:
        for i in range(k):
            if used[i] == 0:
                p[n+1] = permutation[i]
                used[i] = 1
                f(n+1, k, s + golf[p[n]][p[n+1]])
                used[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    golf = [list(map(int, input().split())) for _ in range(N)]

    permutation = list(range(1, N))
    minV = 100 * (N + 1)

    p = [0] + [0] * (N - 1) + [0]
    used = [0] * (N - 1)

    f(0, N - 1, 0)

    print('#{} {}' .format(tc, minV))
```

