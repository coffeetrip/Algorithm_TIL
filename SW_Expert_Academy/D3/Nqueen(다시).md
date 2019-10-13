### 2806. N-Queen

```python
def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and left[i+N-1-j] == 0 and right[i+j] == 0:
                # board[i][j] = 1
                col[j] = 1
                left[i + N - 1 - j] = 1
                right[i + j] = 1
                f(i+1, N)
                col[j] = 0
                left[i + N - 1 - j] = 0
                right[i + j] = 0
                # board[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # board = [[0]*N for _ in range(N)]

    cnt = 0
    col = [0]*N
    right = [0]*2*N
    left = [0]*2*N
    f(0, N)
    print('#{} {}'.format(tc, cnt))
```

```python
def f(n, N, p):
    global cnt
    if n == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if p:
                for idx, j in enumerate(p):
                    if i == j: break # 같은 열 X
                    if abs(j-i) == n-idx: break # 대각선 X
                else:
                    f(n+1, N, p+[i])
            else:
                f(n+1, N, p+[i])
 
for t in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    f(0, N, [])
    print('#{} {}'.format(t, cnt))
```

```python
def find(i, N, left, right, col, l, r, c, board):
    global cnt
    if i == N:  # 모든 줄에 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            # 다른 줄에 j번 열에 퀸이 없어야 하고
            # 왼쪽 대각선과 오른쪽 대각선에 퀸이 없어야 한다.
            # if check(i, j, N):
            if i + j not in left and i - j + N not in right and j not in col:
                board[i][j] = 1
                left[l] = i + j
                right[r] = i - j + N
                col[c] = j
                l += 1
                r += 1
                c += 1
                find(i + 1, N, left, right, col, l, r, c, board)
                board[i][j] = 0
                l -= 1
                r -= 1
                c -= 1
                left[l] = -1
                right[r] = -1
                col[c] = -1
 
 
t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    cnt = 0
    board = [[0] * N for i in range(N)]
    left, right, col = [-1] * (N * N), [-1] * (N * N), [-1] * (N * N)
    l, r, c = 0, 0, 0
    find(0, N, left, right, col, l, r, c, board)
    print("#{} {}".format(tc, cnt))
```

