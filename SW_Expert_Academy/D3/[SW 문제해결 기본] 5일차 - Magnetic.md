# [S/W 문제해결 기본] 5일차 - Magnetic

```
(1) 1개의 열에 대해
(2) N극을 만날때까지 아래로 탐색
- 맨 아랫줄에 다다르면 다음 열에 대해(1)부터 반복
(3) S극 자성체를 만날때까지 아래로 탐색
(4) 맨 아랫줄에 다다르면 다음 열에 대해 (1)부터 반복
(5) 중간에 S극을 만나면 교착 개수를 1증가하고, 다시 해당 위치부터 (2)을 반복
```

```PYTHON
for tc in range(1, 11):  # N 1, S 2
    N = int(input())
    magnetic = [list(input().split()) for _ in range(N)]

    clash = 0  # '12'
    for i in range(N):
        temp = ''
        for j in range(N):
            if magnetic[j][i] != '0':
                temp += magnetic[j][i]
        clash += temp.count('12')

    print('#{} {}' .format(tc, clash))
```

```PYTHON
def f(i, j):
    if table[i][j] == 2:
        return 1
    else:
        ni = i+1
        if ni < N:
            if table[ni][j] == 1:
                return 0
            else:
                if f(ni, j) == 1:
                    return 1
        return 0

T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                if f(i, j) == 1:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))
```



```python
def table_N(j, i, N):
    global magnetic

    if j > 0 and magnetic[j-1][i] == 0:
        if table_N(j-1, i, N) == 1:
            return 1
        else:
        	return 0
    elif j > 0 and magnetic[j-1][i] == 1:
        magnetic[j-1][i] = 0
        return 1
	else:
        return 0

def table_S(j, i, N):
    global magnetic

    if j < N-1 and magnetic[j+1][i] == 0:
        if table_S(j+1, i, N) == 1:
            return 1
    elif j < N-1 and magnetic[j+1][i] == 2:
        magnetic[j+1][i] = 0
        return 1


for T in range(1, 11):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]

    crash = 0
    for i in range(100):
        for j in range(100):
            if magnetic[j][i] == 2:
                J, I = j, i
                if table_N(j, i, N) == 1:
                    crash += 1
              	magnetic[J][I] = 0
            elif magnetic[j][i] == 1:
                J, I = j, i
                if table_S(j, i, N) == 1:
                    crash += 1
                magnetic[J][I] = 0

    print('#{} {}' .format(T, crash))
```

```PYTHON
T = 10
for tc in range(T):
    N = int(input())
    board, check = [], []
    cnt = 0
    for i in range(100):
        board.append(list(map(int, input().split())))
    for i in range(100):
        for j in range(100):
            if board[j][i] != 0:
                check.append(board[j][i])

        # 남쪽으로 떨어질 친구들 치우기
        for c in range(len(check)-1, -1, -1):
            if check[c] == 1:
                check.pop(c)
            else:
                break
        check = check[::-1]
        # 북쪽으로 떨어질 친구들도 치우기
        for c in range(len(check)-1, -1, -1):
            if check[c] == 2:
                check.pop(c)
            else:
                break
        check = check[::-1]
        for c in range(len(check) -1, -1, -1):
            if check[c] == check[c - 1]:
                check.pop(c)
    print('#{} {}'.format(tc + 1, len(check) // 2))
```



