### 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

```
# i, j칸 까지 도착하는 최소 비용의 합

for i in range(1, N):
    for j in range(1, N):
        d[i][j] = min(d[i-1][j], d[i][j-1]) + arr[i][j]
```

```python
def f(i, j, total):
    global array, N, minV

    if minV < total:
        return
    if i == N-1 and j == N-1:
        if minV > total:
            minV = total
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
def perm(n, k):
    global arr, minV
    if n == k:
        s = 0
        s += arr[0][p[0]-1]
        for m in range(k-1):
            s += arr[p[m]-1][p[m+1]-1]
        s += arr[p[-1]-1][0]

        if minV > s:
            minV = s
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = list(range(2, N+1))
    minV = 100000000
    perm(0, N-1)

    print('#{} {}' .format(tc, minV))
```

```python
def make(n, k):
    global places
    global minV
    if n == k:
        one = [0] + places + [0]
        used = 0
        for j in range(len(one) - 1):
            used += energy[one[j]][one[j + 1]]
        if used < minV:
            minV = used
    else:
        for i in range(n, k):
            places[i], places[n] = places[n], places[i]
            make(n+1, k)
            places[i], places[n] = places[n], places[i]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    energy = [list(map(int, input().split())) for i in range(N)]

    places = list(range(1, N))
    minV = 100000000000000
    make(0, N-1)
    print("#{} {}".format(tc, minV))
```

```python
def perm(n, k):
    global minV, array
    if n == k:
        s = 0
        for j in range(len(array)-1):
            if s > minV:
                return
            else:
                s += card[array[j]][array[j+1]]
        if minV > s + card[0][array[0]] + card[array[-1]][0]:
            minV = s + card[0][array[0]] + card[array[-1]][0]
    else:
        for i in range(n, k):
            array[i], array[n] = array[n], array[i]
            perm(n+1, k)
            array[i], array[n] = array[n], array[i]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [list(map(int, input().split())) for _ in range(N)]

    array = list(range(1, N))
    minV = 1000000000
    perm(0, N-1)

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
        if s + table[p[-2] - 1][p[-1] - 1] < minV:
            minV = s + table[p[-2] - 1][p[-1] - 1]
        return
    elif s > minV:
        return
    else:
        for i in range(k):
            if used[i] == 0:
                p[n + 1] = room[i]
                used[i] = 1
                f(n + 1, k, s + table[p[n] - 1][p[n + 1] - 1])
                used[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    room = list(range(2, N + 1))
    minV = 100 * (N + 1)

    p = [1] + [0] * (N - 1) + [1]
    used = [0] * (N - 1)
    f(0, N - 1, 0)
    print(minV)
```







```python
#5일차 백트래킹(시간초과)
def f(n, k):
    global arr, minV
    if n == k:
        s = 0
        for i in range(k):
            if s > minV:
                return
            s += arr[i][p[i]]

        if minV > s:
            minV = s
    else:
        for i in range(n, N):
            p[n], p[i] = p[i], p[n]
            f(n+1, k)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]

    minV = 100000000
    f(0, N)
    print('#{} {}' .format(tc, minV))
```

