- 창용 마을 무리의 개수(상호배타집합) 7465

- 상원이의 생일파티(Dfs/bfs 그래프 탐색) 5521

- 정사각형 방(dfs/bfs/dp 그래프 탐색 응용) 1861

- 인수의 생일 파티(양방향 다익스트라) 1795

- [sw응용]2일차 - 최대상금 1244

  



### 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

```python
# mst - kruskal
def rep(n):
    while  p[n] != n:
        n = p[n]
    return n

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x: x[2])  # 가중치를 기준으로 정렬

    p = [i for i in range(V+1)]   # 대표원소 배열
    cnt = 0
    total = 0
    for x in edge:
        n0 = rep(x[0])
        n1 = rep(x[1])
        if n0 != n1:  # 두 노드의 대표 원소가 다르면 mst에 추가
            p[n1] = n0
            cnt += 1  # 간선을 선택한 경우
            total += x[2]  # 가중치의 합
            if cnt == V:  # N개의 노드(V+1) 가 있는 경우 N-1개의 간선을 선택(V)
                break

    print('#{} {}' .format(tc, total))
```

```python
# mst - prim
T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge = sorted(edge, key=lambda x: x[2])
    total = 0
    # 인접행렬 구하기
    table = [[0] * (N+1) for _ in range(N+1)]
    for eg in edge:
        n1, n2, w = eg
        table[n1][n2] = w
        table[n2][n1] = w
        
    mst = [0] * (N+1)
    mst[0] = 1
    while 1:
        if sum(mst) == N+1:
            break
        idx = 0
        minV = 9999
        for i in range(len(mst)):
            if mst[i] == 1:
                for j in range(N+1):
                    if table[i][j] != 0 and mst[j] == 0:
                        if minV > table[i][j]:
                            minV = table[i][j]
                            idx = j

        total += minV
        mst[idx] = 1
    print("#{} {}".format(t, total))
```

```python
# mst- prim
for t in range(int(input())):
    ans = 0
    last_node, size_line = map(int, input().split())
    relations = {}
    for _ in range(size_line):
        start, end, power = map(int, input().split())
        if relations.get(start):
            relations[start][end] = power
        else:
            relations[start] = {end: power}
        if relations.get(end):
            relations[end][start] = power
        else:
            relations[end] = {start: power}
    checked = [1] + [0] * last_node
    while checked.count(0) != 0:
        temp = "awesome"
        candidate = 100
        for start in range(last_node+1):
            if checked[start]:
                for destination, weight in relations[start].items():
                    if weight < candidate and checked[destination] == 0:
                        temp = destination
                        candidate = weight
        checked[temp] = 1
        ans += candidate
    print("#{} {}".format(t + 1, ans))
```





### 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

```python
def f(i, j):
    global N
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    D = [[999999]*N for _ in range(N)]
    D[i][j] = 0
    queue = [[i, j]]

    while len(queue) != 0:
        x = queue.pop(0)
        for k in range(4):
            ni = x[0] + di[k]
            nj = x[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                diff = 0
                if H[ni][nj] > H[x[0]][x[1]]:
                    diff = H[ni][nj] - H[x[0]][x[1]]
                if D[ni][nj] > D[x[0]][x[1]] + diff + 1:
                    D[ni][nj] = D[x[0]][x[1]] + diff + 1
                    queue.append([ni, nj])
    return D[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    minV = 1000000
    print('#{} {}' .format(tc, f(0, 0)))
```

```python
def find(N):
    global minV
    queue = [[0, 0]]
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    while queue != []:
        col, row = queue.pop(0)
        for i in range(4):
            nc = col + dc[i]
            nr = row + dr[i]
            if 0 <= nc < N and 0 <= nr < N:
                energy = pair[col][row] + 1
                diff = world[nc][nr] - world[col][row]
                if diff >= 1:
                    energy += diff
                if pair[nc][nr] == 0:
                    pair[nc][nr] = energy
                    queue.append([nc, nr])
                else:
                    if pair[nc][nr] > energy:
                        pair[nc][nr] = energy
                        queue.append([nc, nr])
    return pair[-1][-1]


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    world = [list(map(int, input().split())) for i in range(N)]
    pair = [[0]*N for i in range(N)]
    minV = 1000000000000000000000
    res = find(N)
    # print(pair)
    print("#{} {}".format(tc, res))
```

```python
def f(i,j):
    global N, check

    q = []
    q.append([i,j])
    check[i][j] = 0
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and nj >= 0 and ni < N and nj < N:
                s = check[i][j]+1
                if arr[ni][nj]-arr[i][j]>0:
                    s += arr[ni][nj]-arr[i][j]
                if check[ni][nj] > s:
                    check[ni][nj] = s
                    q.append([ni, nj])


di = [0,1,0,-1]
dj = [1,0,-1,0]

for t in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [[float('INF')]*N for i in range(N)]
    f(0,0)

    print('#{} {}'.format(t+1, check[-1][-1]))
```

```python
func = [lambda x: [x[0] + 1, x[1]], lambda x: [x[0] - 1, x[1]], lambda x: [x[0], x[1] + 1], lambda x: [x[0], x[1] - 1]]

for t in range(int(input())):
    ans = 0
    size_table = int(input())
    table = [list(map(int, input().split())) for _ in range(size_table)]
    data = [[-1 for _ in range(size_table)] for __ in range(size_table)]
    stack = [[0, 0]]
    data[0][0] = 0
    while stack:
        temp = []
        while stack:
            start = stack.pop()
            last_table = table[start[1]][start[0]]
            last_data = data[start[1]][start[0]]
            for f in func:
                x, y = f(start)
                if 0 <= x < size_table and 0 <= y < size_table:
                    height_diff = table[y][x] - last_table
                    new_value = last_data + 1 + (height_diff if height_diff > 0 else 0)
                    if data[y][x] == -1:
                        data[y][x] = new_value
                        temp.append([x, y])
                    else:
                        if data[y][x] > new_value:
                            data[y][x] = new_value
                            temp.append([x, y])
        stack = temp
    print("#{} {}".format(t + 1, data[size_table - 1][size_table - 1]))
```





### 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

```python
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    arr = [[10*E+1]*(N+1) for _ in range(N+1)]

    for i in range(N+1):
        arr[i][i] = 0

    for e in edge:
        r = e[0]
        c = e[1]
        arr[r][c] = e[2]

    D = arr[0]   # 거리
    V = set(range(N+1))  # 정점 집합
    U = {0}   # 선택된 정점 집합

    while U != V:
        B = V - U    # D[w]가 최소인 정점 w
        minV = 10*E+1
        for b in B:
            if minV > D[b]:
                minV = D[b]
                minidx = b
        U.add(minidx)
        for w in range(N+1):  # w에 인접한 모든 정점 v
            if arr[minidx][w] != 0 and arr[minidx][w] != 10*E+1:
                D[w] = min(D[w], (D[minidx]+arr[minidx][w]))

    print('#{} {}'.format(tc, D[N]))
```

```python
# def find(s, A, D):
#     global N, E
#     U = {s}
#     V = set(range(N + 1))
#     for v in range(N + 1):
#         D[v] = A[s][v]
#     while U != V:
#         minV = 100000000000000
#         for i in V - U:
#             if D[i] < minV:
#                 minV = D[i]
#                 w = i
#         # w = D.index(min([D[i] for i in V - U]))
#         U.add(w)
#         for v in range(N + 1):
#             if 0 < A[w][v] < 10001:
#                 D[v] = min(D[v], D[w] + A[w][v])



t = int(input())
for tc in range(1, t + 1):
    N, E = map(int, input().split())
    sew = [list(map(int, input().split())) for i in range(E)]
    near = [[10001] * (N + 1) for i in range(N + 1)]
    for i in sew:
        near[i[0]][i[1]] = i[2]
    for i in range(N + 1):
        near[i][i] = 0
    D = near[0]
    U = {0}
    V = set(range(N + 1))
    while U != V:
        minV = 100000000000000
        for i in V - U:
            if D[i] < minV:
                minV = D[i]
                w = i
        U.add(w)
        for v in range(N + 1):
            if 0 < near[w][v] < 10001:
                D[v] = min(D[v], D[w] + near[w][v])
    print("#{} {}".format(tc, D[-1]))
```

```python
T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())

    # 인접행렬 생성
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w  # s -> e 로 가는 가중치

    V = {i for i in range(N + 1)}
    U = {0}  # 선택된 정점집합. 시작부분 포함하기

    D = [0] * (N + 1)  # 거리들
    for v in V - U:
        weight = adj[0][v]
        if weight == 0:  # 못가는곳
            D[v] = 11  # 될 수 있는한 최대(무한대개념)
        else:
            D[v] = weight

    while U != V:
        # 안고른 노드들 중, 최소를 찾는다.
        w = None
        minimum_w = 11
        for node in V - U:
            if D[node] <= minimum_w:
                w = node
                minimum_w = D[node]

        U = U | {w}  # 최소 노드 포함

        for i in range(N + 1):
            v = adj[w][i]  # 인접 정점의 가중치
            if 0 < v < 11:  # 인접하면,
                D[i] = min(D[i], D[w] + v)  # 비교

    print("#{} {}".format(tc, D[N]))
```

```python
for T in range(int(input())):
    N, E = map(int, input().split())

    nodes = [0] + [10 * 10000000] * N
    for i in range(E):
        s, e, l = map(int, input().split())

        t = nodes[s] + l
        if nodes[e] > t:
            nodes[e] = t
    print('#{} {}'.format(T + 1, nodes[N]))
```

