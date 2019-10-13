### [S/W 문제해결 응용] 7일차 - 행렬찾기

```python
def f(si, sj):
    global arr, visited, N
    q = [[si, sj]]
    visited[si][sj] = 1

    di, dj = [0, 1], [1, 0]
    while len(q) != 0:
        n = q.pop(0)
        for k in range(2):
            ni = n[0] + di[k]
            nj = n[1] + dj[k]
            if ni < N and nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 0:
                visited[ni][nj] = 1
                q.append([ni, nj])
                ei, ej = ni, nj

    return [ei-si+1, ej-sj+1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    temp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and visited[i][j] == 0:
                temp.append(f(i, j))

    temp.sort(key=lambda x:(x[0]*x[1], x[0]))

    print('#{} {}' .format(tc, len(temp)), end=" ")
    for i in temp:
        print(i[0], i[1], end=" ")
    print()
```



```python
def find(si, sj, N):
    global arr
    row, col = 1, 1
    ni, nj = si, sj
    for _ in range(N):
        ni += 1
        if ni < N and arr[ni][sj]:
            row += 1
        else:
            break
            
    for _ in range(N):
        nj += 1
        if nj < N and arr[si][nj]:
            col += 1
        else:
            break
            
    for i in range(si, ni):
        for j in range(sj, nj):
            arr[i][j] = 0
    return row, col

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                result.append(find(i, j, N))
    result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    
    print('#{} {}'.format(tc, len(result)), end=' ')
    for i in result:
        print(i[0], i[1], end=' ')
    print()
```

```python
def f(i, j): # i, j = 0이 아닌 처음 수
    global arr
    global visited
    q = []
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited[i][j] = 1
    q.append([i, j])
 
    while len(q) != 0:
        n = q.pop(0)
        i = n[0]
        j = n[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<N and nj>=0 and nj<N:
                if arr[ni][nj] !=0 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append([ni, nj])
                    lastI = ni
                    lastJ = nj
 
    return lastI, lastJ
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    q = []
    r = [] # [세로길이 * 가로길이]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] != 0:
                startI, startJ = i, j
                lastI, lastJ = f(startI, startJ)
                r.append([lastI-startI+1, lastJ-startJ+1])
    # print(r)
    result = sorted(r, key = lambda x: (x[0]*x[1], x[0]))
    # print(result)
    print('#{}'.format(tc), end=' ')
    print(len(r), end=' ')
    for k in result:
        print(k[0], k[1], end=' ')
    print()
```

```python
t = int(input())
for tc in range(1, t+1):
    N = int(input())
    space = [list(map(int, input().split())) for i in range(N)]
    resultstack = []
 
    for i in range(N):
        for j in range(N):
            if space[i][j] != 0:    # 만나면 가로세로 길이 추출
                rowcnt = 0
                colcnt = 0
                for k in range(j, N):
                    if space[i][k] == 0:
                        break
                    rowcnt += 1
                for l in range(i, N):
                    if space[l][j] == 0:
                        break
                    colcnt += 1
 
                resultstack.append([rowcnt, colcnt])
 
                # 만난 네모 제거
                rstack = []
                rstack.append([i,j])
                di = [0, 1, 0, -1]
                dj = [1, 0, -1, 0]
                while rstack != []:
                    get = rstack.pop()
                    ｋi, ｋj = get[0], get[1]
                    space[ｋi][ｋj] = 0
                    for dir in range(4):
                        ni = ｋi + di[dir]
                        nj = ｋj + dj[dir]
 
                        if 0 <= ni < N and 0 <= nj < N:
                            if space[ni][nj]:
                                rstack.append([ni, nj])
                # print(space)
 
 
    # 출력
    res = sorted(resultstack, key=lambda res: (res[0]*res[1], res[1]))
    print("#{} {}".format(tc, len(res)), end=" ")
    for r in res:
        print(*reversed(r), end=" ")
    print()
```

```python
def f(i, j):
    global visited, i_len, j_len
    visited[i][j] = 1

    ni = i + 1
    if ni < N and arr[ni][j] != 0 and visited[ni][j] == 0:
        visited[ni][j] = 1
        i_len += 1
        f(ni, j)

    nj = j + 1
    if nj < N and arr[i][nj] != 0 and visited[i][nj] == 0:
        visited[i][nj] = 1
        j_len += 1
        f(i, nj)

    return [i_len, (j_len+i_len)//i_len, i_len*((j_len+i_len)//i_len)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    temp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                i_len, j_len = 1, 0
                temp.append(f(i, j))

    temp.sort(key=lambda x: (x[0], x[2]))

    print('#{} {}' .format(tc, len(temp)), end=" ")
    for i in range(len(temp)):
        for j in range(2):
            print(temp[i][j], end=" ")
    print()
```

